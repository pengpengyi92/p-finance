"""Offline index, generated-page and cross-topic publication contracts."""

from collections import Counter
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "finance_topics", ROOT / "scripts" / "render_finance_repository_topics.py"
)
TOPICS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOPICS)


class FinanceTopicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(TOPICS.LEDGER.read_text(encoding="utf-8"))
        cls.rows = {row["repo"].casefold(): row for row in cls.data["repositories"]}

    def test_pins_and_scope(self):
        TOPICS.validate(self.data)
        self.assertGreaterEqual(len(self.rows), 100)
        for plan in self.data["topics"]:
            self.assertTrue(any(plan in row["topics"] for row in self.rows.values()))
        self.assertIn("not_included", self.data)

    def test_rejects_invalid_pin_alias_private_and_escape(self):
        for field, value in (
            ("head", "main"),
            ("visibility", "PRIVATE"),
            ("readme", "../README.md"),
            ("license_file", "https://example.net/LIC"),
        ):
            data = deepcopy(self.data)
            data["repositories"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                TOPICS.validate(data)
        data = deepcopy(self.data)
        alias = deepcopy(data["repositories"][0])
        alias["repo"] = alias["repo"].upper()
        data["repositories"].append(alias)
        with self.assertRaisesRegex(ValueError, "duplicate canonical pin"):
            TOPICS.validate(data)

    def test_existing_cb_and_ib_routes_remain_covered(self):
        old = json.loads((ROOT / "repo/banking-capital/catalog.json").read_text(encoding="utf-8"))
        for row in old["repositories"]:
            for long_name, track in (("corporate-banking", "CB"), ("investment-banking", "IB")):
                if long_name in row["categories"]:
                    self.assertIn(track, self.rows[row["repository"].casefold()]["topics"], row["repository"])

    def test_cross_list_preserves_use_and_canonical_name(self):
        fig = self.rows["prowide/prowide-iso20022"]["topics"]
        self.assertEqual(set(fig), {"CB", "AC"})
        self.assertIn("现金", fig["CB"]["use"])
        self.assertIn("交收", fig["AC"]["use"])
        self.assertEqual(set(self.rows["finos/common-domain-model"]["topics"]), set(TOPICS.PAGES))
        self.assertNotIn("domokane/financepy", self.rows)
        self.assertIn("financepy-org/financepy", self.rows)

    def test_custody_and_rights_controls(self):
        self.assertEqual(self.rows["digital-asset/canton"]["topics"]["AC"]["lane"], "token")
        self.assertEqual(self.rows["prowide/prowide-core"]["topics"]["AC"]["lane"], "messages")
        self.assertIn("不是 Fedwire Securities", self.rows["moov-io/fedwire20022"]["topics"]["AC"]["use"])
        self.assertTrue(TOPICS.read_only(self.rows["attack68/rateslib"]))
        self.assertTrue(TOPICS.read_only(self.rows["hyperledger-labs/harmonia"]))
        self.assertTrue(TOPICS.read_only({**self.rows["finos/legend"], "license": "UNKNOWN"}))

    def test_rendered_navigation_and_links(self):
        TOPICS.run(check=True)
        for track, page in TOPICS.PAGES.items():
            path = ROOT / "repo" / page
            content = path.read_text(encoding="utf-8")
            repos = re.findall(r"(?m)^\| \[`([A-Za-z0-9_./-]+)`\]\(https://github\.com/", content)
            expected = [row["repo"] for row in self.rows.values() if track in row["topics"]]
            self.assertEqual(Counter(repos), Counter(expected), page)
            self.assertIn("NOT_RUN / UNMEASURED", content)
            for href in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", content):
                if not href.startswith("https://"):
                    target = (path.parent / unquote(href.split("#", 1)[0])).resolve()
                    self.assertTrue(target.is_relative_to(ROOT), href)
                    self.assertTrue(target.exists(), (page, href))
            for nav in (ROOT / "repo/README.md", ROOT / "README.md", ROOT / "AGENTS.md"):
                self.assertIn(page, nav.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
