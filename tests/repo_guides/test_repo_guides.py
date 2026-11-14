"""Offline catalog contracts; no third-party model installation or evaluation."""
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / "repo"
CARDS = {
    "JerBouma/FinanceToolkit": "corporate-finance/finance-toolkit.md",
    "numpy/numpy-financial": "corporate-finance/numpy-financial.md",
    "lballabio/QuantLib": "ficc/quantlib.md",
    "tradingtechnologies/Strata": "ficc/strata.md",
    "domokane/FinancePy": "ficc/financepy.md",
    "OpenSourceRisk/Engine": "ficc/ore.md",
    "goldmansachs/gs-quant": "ficc/gs-quant.md",
    "attack68/rateslib": "ficc/rateslib.md",
}
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)\)")
PRIVATE_DRIVE = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]")


class RepoGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads((REPO / "source_snapshot.json").read_text(encoding="utf-8"))["repositories"]
        cls.sources = {r["repository"]: r for r in cls.rows}

    def test_eight_public_pinned_sources(self):
        self.assertEqual(len(self.rows), 8)
        self.assertEqual(set(self.sources), set(CARDS))
        for row in self.rows:
            self.assertFalse(row["private"])
            self.assertFalse(row["tree_truncated"])
            self.assertRegex(row["head"], r"^[a-f0-9]{40}$")
            self.assertTrue(row["observed_at"].endswith("+08:00"))
            self.assertIn(row["readme_path"], row["source_paths"])
            self.assertIn(row["license_path"], row["source_paths"])

    def test_each_card_is_actionable_and_bounded(self):
        for name, filename in CARDS.items():
            text = (REPO / filename).read_text(encoding="utf-8")
            for required in ("Last reviewed", "2026-11-14", "## 用途", "## 先读", "## 练习（未执行）", "## Our public contribution", "## Boundaries", self.sources[name]["head"]):
                self.assertIn(required, text, filename)
            self.assertIn("https://github.com/" + name, text)

    def test_local_markdown_targets_exist_and_stay_inside_project(self):
        for path in REPO.rglob("*.md"):
            for href in LINK.findall(path.read_text(encoding="utf-8")):
                if re.match(r"[a-z]+:", href) or href.startswith("#"):
                    continue
                target = (path.parent / unquote(href.split("#", 1)[0])).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()), (path, href))
                self.assertTrue(target.exists(), (path, href))

    def test_pinned_source_links_match_captured_tree(self):
        count = 0
        for path in REPO.rglob("*.md"):
            for href in LINK.findall(path.read_text(encoding="utf-8")):
                m = re.fullmatch(r"https://github.com/([^/]+/[^/]+)/blob/([a-f0-9]{40})/(.+)", href)
                if not m:
                    continue
                name, sha, filename = m.groups()
                self.assertIn(name, self.sources)
                row = self.sources[name]
                self.assertEqual(sha, row["head"])
                self.assertIn(filename, row["source_paths"], href)
                count += 1
        self.assertGreaterEqual(count, 30)

    def test_contribution_types_and_statuses_are_not_pooled(self):
        ft = self.sources["JerBouma/FinanceToolkit"]["contributions"]
        self.assertEqual({r["number"] for r in ft}, set(range(425, 430)))
        self.assertTrue(all(r["type"] == "PR" and r["state"] == "MERGED" and r["merged_at"] for r in ft))
        self.assertTrue(all(r["author"] == "pengpengyi92" for row in self.rows for r in row["contributions"]))
        ql = self.sources["lballabio/QuantLib"]["contributions"][0]
        self.assertEqual((ql["type"], ql["state"]), ("ISSUE", "CLOSED"))
        rates = self.sources["attack68/rateslib"]["contributions"][0]
        self.assertEqual((rates["type"], rates["state"]), ("DISCUSSION", "UNANSWERED"))
        allowed = {r["url"] for row in self.rows for r in row["contributions"]}
        for filename in CARDS.values():
            for href in LINK.findall((REPO / filename).read_text(encoding="utf-8")):
                if re.search(r"/(pull|issues|discussions)/\d+$", href):
                    self.assertIn(href, allowed)

    def test_license_exception_and_unmeasured_exercises_stay_visible(self):
        rates = (REPO / CARDS["attack68/rateslib"]).read_text(encoding="utf-8")
        self.assertIn("not open source", rates)
        self.assertNotIn("pip install", rates)
        index = (REPO / "README.md").read_text(encoding="utf-8")
        self.assertIn("llmquant.md", index)
        self.assertIn("Source-available, not open source", index)
        self.assertIn("未安装/运行", index)
        self.assertIn("UNMEASURED", (REPO / "ficc/README.md").read_text(encoding="utf-8"))

    def test_no_private_workstation_or_credential_material(self):
        patterns = (PRIVATE_DRIVE, r"github_pat_[A-Za-z0-9_]{30,}", r"gh[pousr]_[A-Za-z0-9]{30,}", r"file://")
        files = [REPO / p for p in CARDS.values()] + [REPO / "README.md", REPO / "source_snapshot.json", REPO / "HOW_TO_STUDY.md"]
        for path in files:
            text = path.read_text(encoding="utf-8")
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, text), path.name)

    def test_private_drive_detection_does_not_match_https(self):
        self.assertIsNone(PRIVATE_DRIVE.search("https://github.com/example/repo"))
        self.assertIsNotNone(PRIVATE_DRIVE.search("local C:/private/work"))
        self.assertIsNotNone(PRIVATE_DRIVE.search(r"local E:\private\work"))


if __name__ == "__main__":
    unittest.main()
