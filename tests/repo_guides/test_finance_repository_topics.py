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
        self.assertEqual(set(self.rows["finos/common-domain-model"]["topics"]),
                         set(TOPICS.ORIGINAL_PAGES) | {"SEC", "EX"})
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
            navigators = ((ROOT / "repo/README.md", ROOT / "README.md", ROOT / "AGENTS.md")
                          if track in TOPICS.ORIGINAL_PAGES else (ROOT / "repo" / TOPICS.MARKET_MAP,))
            for nav in navigators:
                self.assertIn(page, nav.read_text(encoding="utf-8"))

    def test_direct_discussions_are_distinct_and_navigable(self):
        repo_index = (ROOT / "repo/README.md").read_text(encoding="utf-8")
        numbers = []
        for track, page in TOPICS.ORIGINAL_PAGES.items():
            number = self.data["topics"][track]["discussion"]
            numbers.append(number)
            href = f"{TOPICS.FORUM}/{number}"
            self.assertIn(f"]({href})", (ROOT / "repo" / page).read_text(encoding="utf-8"))
            self.assertIn(f"]({href})", repo_index)
        self.assertEqual(len(set(numbers)), len(TOPICS.ORIGINAL_PAGES))
        bad = deepcopy(self.data)
        bad["topics"]["CB"]["discussion"] = bad["topics"]["IB"]["discussion"]
        with self.assertRaisesRegex(ValueError, "distinct public discussion"):
            TOPICS.validate(bad)

    def test_expandable_groups_preserve_numbering_and_cross_listing(self):
        content = (ROOT / "repo" / TOPICS.MARKET_MAP).read_text(encoding="utf-8")
        groups = re.findall(r"<details>\n<summary>(.*?)（(\d+)）</summary>\n(.*?)\n</details>", content, re.S)
        self.assertEqual([label for label, _, _ in groups], list(TOPICS.GROUPS))
        for label, count, body in groups:
            tracks = TOPICS.GROUPS[label]
            entries = re.findall(r"(?m)^(\d+)\. \[`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`\]", body)
            expected = {row["repo"] for row in self.rows.values() if set(tracks) & set(row["topics"])}
            self.assertEqual(int(count), len(expected), label)
            self.assertEqual(Counter(name for _, name in entries), Counter(expected), label)
            self.assertEqual([int(n) for n, _ in entries], list(range(1, len(expected) + 1)))
        for path in ("README.md", "repo/README.md", "AGENTS.md"):
            self.assertIn(TOPICS.MARKET_MAP, (ROOT / path).read_text(encoding="utf-8"))

    def test_new_readme_and_license_are_pinned_separately(self):
        new = [row for row in self.rows.values() if "observed_at" in row]
        self.assertGreaterEqual(len(new), 50)
        for row in new:
            self.assertRegex(row["readme_blob"], TOPICS.SHA)
            if row["license_file"]:
                self.assertRegex(row["license_blob"], TOPICS.SHA)
            else:
                self.assertTrue(TOPICS.read_only(row))
        bad = deepcopy(self.data)
        added = next(row for row in bad["repositories"] if "observed_at" in row)
        added["readme_blob"] = "master"
        with self.assertRaisesRegex(ValueError, "pinned readme_blob"):
            TOPICS.validate(bad)

    def test_provider_and_market_boundaries(self):
        wrapper = self.rows["underloam/xbbg"]
        self.assertEqual(wrapper["topics"]["DATA"]["lane"], "licensed")
        self.assertTrue(TOPICS.read_only(wrapper))
        self.assertEqual(self.rows["coinbase/coinbase-advanced-py"]["topics"]["EX"]["lane"], "digital")
        self.assertEqual(self.rows["enewhuis/liquibook"]["topics"]["EX"]["lane"], "matching")
        self.assertEqual(self.rows["oasislmf/oasispiwind"]["topics"]["INS"]["lane"], "cat")
        for unverified in ("windquant/windpy", "qichacha/qcc-openapi"):
            self.assertNotIn(unverified, self.rows)

    def test_academic_paper_uses_formal_source_and_distinguishes_a_proposed_reproduction(self):
        paper = (ROOT / "paper/README.md").read_text(encoding="utf-8")
        academic = ROOT / "paper/academic"
        index = (academic / "README.md").read_text(encoding="utf-8")
        card = (academic / "alpha-gpt.md").read_text(encoding="utf-8")
        for document in (paper, index, card):
            self.assertIn(f"]({TOPICS.FORUM}/15)", document)
        self.assertIn("academic/README.md", paper)
        self.assertIn("(alpha-gpt.md)", index)
        self.assertIn("https://aclanthology.org/2025.emnlp-demos.14/", card)
        self.assertIn("https://doi.org/10.18653/v1/2025.emnlp-demos.14", card)
        self.assertIn("https://arxiv.org/abs/2308.00016", card)
        self.assertIn("System Demonstrations", card)
        self.assertIn("NOT_RUN", card)
        self.assertFalse(list(academic.glob("*.pdf")))


if __name__ == "__main__":
    unittest.main()
