"""Offline provenance, ownership and rights contracts for the banking catalog."""
from datetime import datetime
import importlib.util
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "repo" / "banking-capital"
SPEC = importlib.util.spec_from_file_location("banking_collector", ROOT / "scripts" / "collect_banking_capital_repos.py")
COLLECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COLLECTOR)


class BankingCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((CATALOG / "catalog.json").read_text(encoding="utf-8"))
        cls.snapshot = json.loads((CATALOG / "snapshot.json").read_text(encoding="utf-8"))

    def test_full_four_bank_pagination_and_public_boundary(self):
        orgs = self.snapshot["institutions"]
        self.assertEqual({x["organization"] for x in orgs}, {"goldmansachs", "jpmorganchase", "morganstanley", "deutschebank"})
        inventory = []
        for org in orgs:
            self.assertTrue(org["pagination_complete"])
            self.assertGreaterEqual(org["pages_read"], 1)
            self.assertTrue(org["repositories"])
            for row in org["repositories"]:
                self.assertFalse(row["private"])
                self.assertFalse(row["fork"])
                self.assertEqual(row["repository"].split("/")[0].casefold(), org["organization"])
                inventory.append(row["repository"].casefold())
        self.assertEqual(len(inventory), len(set(inventory)))

    def test_selected_sources_are_unique_pinned_and_timestamped(self):
        rows = self.snapshot["repositories"]
        self.assertEqual(len(rows), len(self.config["repositories"]))
        self.assertGreaterEqual(len(rows), 40)
        self.assertEqual(len(rows), len({x["repository"].casefold() for x in rows}))
        for row in rows + self.snapshot["reference_only"]:
            self.assertFalse(row["private"])
            self.assertRegex(row["head"], r"^[a-f0-9]{40}$")
            self.assertEqual(datetime.fromisoformat(row["observed_at"]).utcoffset().total_seconds(), 28800)
            self.assertEqual(row["validation"], "PUBLIC_SOURCE_REVIEW_NOT_EXECUTED")
            for source in row["sources"]:
                self.assertIn("/blob/" + row["head"] + "/", source["url"])
                self.assertRegex(source["blob_sha"], r"^[a-f0-9]{40}$")

    def test_categories_and_attribution_cannot_be_inferred_from_brand(self):
        covered = set()
        banks = {x["organization"] for x in self.config["institutions"]}
        rows = {x["repository"]: x for x in self.snapshot["repositories"]}
        for row in rows.values():
            covered.update(row["categories"])
            self.assertTrue(row["use"])
            self.assertTrue(row["boundary"])
            if row["relationship"] == "bank-owned":
                self.assertIn(row["repository"].split("/")[0].casefold(), banks)
        self.assertEqual(covered, set(COLLECTOR.CATEGORIES))
        self.assertEqual(rows["finos/legend"]["relationship"], "foundation-project")
        self.assertNotEqual(rows["perspective-dev/perspective"]["relationship"], "bank-owned")
        self.assertEqual(rows["EQTPartners/CompanyKG"]["relationship"], "pe-firm-owned")

    def test_license_negative_controls(self):
        for signal in (None, "NOASSERTION", "BUSL-1.1", "LicenseRef-Proprietary"):
            self.assertEqual(COLLECTOR.license_class(signal), "needs-license-review")
        self.assertEqual(COLLECTOR.license_class("Community-Spec-1.0"), "specification-terms")
        self.assertEqual(COLLECTOR.license_class("AGPL-3.0"), "reciprocal-signal-review-text")
        for row in self.snapshot["repositories"]:
            self.assertEqual(row["license_class"], COLLECTOR.license_class(row["license_signal"]))

    def test_no_license_references_stay_out_of_reuse_routes(self):
        selected = {x["repository"] for x in self.snapshot["repositories"]}
        refs = self.snapshot["reference_only"]
        self.assertTrue(refs)
        self.assertFalse(selected & {x["repository"] for x in refs})
        for row in refs:
            self.assertTrue(row["reason"])
        page = (CATALOG / "reference-only.md").read_text(encoding="utf-8")
        self.assertIn("not an open-source license", page)

    def test_local_links_and_primary_pins(self):
        allowed = {source["url"] for row in self.snapshot["repositories"] + self.snapshot["reference_only"] for source in row["sources"]}
        observed = set()
        for path in CATALOG.glob("*.md"):
            for href in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                if href.startswith("https://github.com/") and "/blob/" in href:
                    self.assertIn(href, allowed)
                    observed.add(href)
                elif not re.match(r"[a-z]+:", href) and not href.startswith("#"):
                    target = (path.parent / unquote(href.split("#", 1)[0])).resolve()
                    self.assertTrue(target.is_relative_to(ROOT.resolve()))
                    self.assertTrue(target.exists(), (path.name, href))
        self.assertEqual(observed, allowed)

    def test_public_only_no_private_workstation_material(self):
        paths = list(CATALOG.glob("*.json")) + list(CATALOG.glob("*.md"))
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for pattern in (r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]", r"github_pat_[A-Za-z0-9_]{30,}", r"gh[pousr]_[A-Za-z0-9]{30,}", r"file://"):
                self.assertIsNone(re.search(pattern, text), path.name)

    def test_private_repository_negative_control(self):
        with self.assertRaises(ValueError):
            COLLECTOR.metadata({"private": True})

    def test_raw_sources_cannot_be_written_into_public_report(self):
        with patch.object(COLLECTOR.subprocess, "run") as run:
            with self.assertRaises(ValueError):
                COLLECTOR.collect(ROOT / "report" / "raw-review")
            run.assert_not_called()

    def test_market_data_and_execution_limits_remain_explicit(self):
        self.assertIn("UNMEASURED", self.snapshot["execution"])
        rows = {x["repository"]: x for x in self.snapshot["repositories"]}
        self.assertIn("权益", rows["jpmorganchase/fusion"]["boundary"])
        self.assertIn("AGPL", rows["captableinc/captable"]["boundary"])
        self.assertIn("数据", rows["EQTPartners/CompanyKG"]["boundary"])

    def test_empty_repository_is_inventory_only(self):
        rows = {x["repository"]: x for x in self.snapshot["repositories"]}
        empty = {x["repository"]: x for x in self.snapshot["inventory_only"]}
        self.assertNotIn("deutschebank/dbcore", rows)
        self.assertEqual(empty["deutschebank/dbcore"]["size_kb"], 0)
        self.assertNotIn("head", empty["deutschebank/dbcore"])
        self.assertIn("Code Components", rows["Open-Cap-Table-Coalition/Open-Cap-Format-OCF"]["license_note"])

    def test_resume_keeps_actual_observation_time(self):
        import hashlib

        endpoint = "repos/example/public"
        observed = "2026-11-14T01:02:03+08:00"
        with TemporaryDirectory() as directory:
            cache = Path(directory)
            (cache / (hashlib.sha256(endpoint.encode()).hexdigest() + ".json")).write_text(
                json.dumps({"observed_at": observed, "response": {"private": False}}), encoding="utf-8"
            )
            with patch.object(COLLECTOR, "CACHE_DIR", cache), patch.object(COLLECTOR, "RESUME", True), patch.object(COLLECTOR.subprocess, "run") as run:
                self.assertEqual(COLLECTOR.api(endpoint), {"private": False})
                self.assertEqual(COLLECTOR.OBSERVED_AT[endpoint], observed)
                run.assert_not_called()

    def test_access_failure_is_not_a_missing_optional_license(self):
        failure = subprocess.CompletedProcess(["gh"], 1, "", "gh: Forbidden (HTTP 403)")
        with patch.object(COLLECTOR, "CACHE_DIR", None), patch.object(COLLECTOR.subprocess, "run", return_value=failure), patch.object(COLLECTOR.time, "sleep"):
            with self.assertRaises(RuntimeError):
                COLLECTOR.api("repos/example/public/license", optional=True)


if __name__ == "__main__":
    unittest.main()
