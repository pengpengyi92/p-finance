"""Render the public finance directory from one reviewed source ledger."""

from argparse import ArgumentParser
from datetime import datetime, timedelta
import json
from pathlib import Path
import re
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "repo" / "finance-topics.json"
REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
SHA = re.compile(r"[a-f0-9]{40}")
FORUM = "https://github.com/pengpengyi92/p-finance/discussions"
ORIGINAL_PAGES = {
    "CB": "corporate-banking/README.md",
    "IB": "investment-banking/README.md",
    "FICC": "ficc/catalog.md",
    "AC": "asset-custody/README.md",
}
PAGES = ORIGINAL_PAGES | {
    "WM": "wealth-management/README.md",
    "PE": "private-equity/README.md",
    "VC": "venture-capital/README.md",
    "SEC": "securities/README.md",
    "EX": "exchanges/README.md",
    "FUND": "funds/README.md",
    "INS": "insurance/README.md",
    "DATA": "financial-data/README.md",
}
MARKET_MAP = "market-map.md"
GROUPS = {
    "Bank / 银行": ("CB", "IB", "FICC", "AC", "WM"),
    "PE / 私募股权": ("PE",),
    "VC / 创业投资": ("VC",),
    "Securities / 券商与证券": ("SEC",),
    "Exchange / 交易所": ("EX",),
    "Fund / 基金与资产管理": ("FUND",),
    "Insurance / 保险": ("INS",),
    "Financial Data / 金融数据与企业信息": ("DATA",),
}


def source_links(row):
    base = f"https://github.com/{row['repo']}"
    tree = f"{base}/tree/{row['head']}"
    blob = f"{base}/blob/{row['head']}/"
    readme = row["readme"]
    license_file = row["license_file"]
    return (
        f"[README]({blob + quote(readme)})" if readme else f"[固定源码树]({tree})",
        f"[许可文件]({blob + quote(license_file)})" if license_file else (
            f"[许可目录]({tree + '/' + quote(row['license_dir'])})" if row.get("license_dir") else "许可入口未核实"
        ),
    )


def validate(data):
    original = datetime.fromisoformat(data["observed_at"])
    if data["schema_version"] != 1 or original.utcoffset() != timedelta(hours=8):
        raise ValueError("A versioned UTC+08:00 snapshot is required")
    names = set()
    plans = data["topics"]
    if {track: plan["page"] for track, plan in plans.items()} != PAGES:
        raise ValueError("Unexpected finance topic paths")
    expanded = datetime.fromisoformat(data["expanded_at"])
    if expanded.utcoffset() != timedelta(hours=8) or expanded < original:
        raise ValueError("Expansion must follow the original UTC+08:00 snapshot")
    discussion_numbers = [plan["discussion"] for plan in plans.values() if "discussion" in plan]
    if (any("discussion" not in plans[track] for track in ORIGINAL_PAGES)
            or any(type(number) is not int or number < 1 for number in discussion_numbers)
            or len(set(discussion_numbers)) != len(discussion_numbers)):
        raise ValueError("Expected distinct public discussion numbers; original discussions are required")
    for row in data["repositories"]:
        full = row["repo"]
        if not REPO.fullmatch(full) or full.casefold() in names or not SHA.fullmatch(row["head"]):
            raise ValueError(f"Invalid or duplicate canonical pin: {full}")
        names.add(full.casefold())
        if row["visibility"] != "PUBLIC" or type(row["archived"]) is not bool or type(row["fork"]) is not bool:
            raise ValueError(f"Missing public/state evidence for {full}")
        for field in ("readme", "license_file", "license_dir"):
            path = row.get(field)
            if path and not re.fullmatch(r"[A-Za-z0-9_. -]+(?:/[A-Za-z0-9_. -]+)*", path):
                raise ValueError(f"Unsafe upstream path: {path}")
            if path and any(part in {".", ".."} for part in path.split("/")):
                raise ValueError(f"Relative upstream path: {path}")
        if "observed_at" in row:
            observation = datetime.fromisoformat(row["observed_at"])
            if observation.utcoffset() != timedelta(hours=8) or not original <= observation <= expanded:
                raise ValueError(f"Invalid source observation time: {full}")
            for path, blob in (("readme", "readme_blob"), ("license_file", "license_blob")):
                if bool(row.get(path)) != bool(row.get(blob)) or (row.get(blob) and not SHA.fullmatch(row[blob])):
                    raise ValueError(f"Missing or invalid pinned {blob}: {full}")
            if not row.get("readme"):
                raise ValueError(f"New entries require a pinned README: {full}")
        if not row["topics"]:
            raise ValueError(f"Missing topic for {full}")
        for track, note in row["topics"].items():
            if track not in plans or note["lane"] not in plans[track]["lanes"] or not note["use"].strip() or "\n" in note["use"]:
                raise ValueError(f"Bad topic lane or use: {full} / {track}")
    if {r["repo"].casefold() for r in data["not_included"]} & names:
        raise ValueError("Excluded and included IDs must be disjoint")


def read_only(row):
    signal = row["license"]
    return row["archived"] or bool(row.get("rights_note")) or signal in {"NOASSERTION", "UNKNOWN"} or not (
        row.get("license_file") or row.get("license_dir")
    )


def render_topic(data, track):
    plan = data["topics"][track]
    rows = [r for r in data["repositories"] if track in r["topics"]]
    discussion = plan.get("discussion")
    forum = f"{FORUM}/{discussion}" if discussion else f"{FORUM}/categories/repo"
    discussion_label = f"本专题讨论 #{discussion}" if discussion else "Repo Discussions"
    lines = [
        f"# {plan['title']}",
        "",
        f"**目录更新：** {data['expanded_at']}（Asia/Shanghai） · **本专题：** {len(rows)} 个公开仓库。",
        "",
        plan["intro"],
        "",
        f"[Repo 总目录](../README.md) · [可展开行业目录](../{MARKET_MAP}) · "
        f"[公开来源账本](../finance-topics.json) · [{discussion_label}]({forum})",
        "",
        "这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；"
        "逐条快照见账本。同一仓库可跨专题，每页解释该用途。",
        "",
        "## 起步路线",
        "",
        *[f"- {note}" for note in plan["guide"]],
    ]
    for key, title in plan["lanes"].items():
        subset = [r for r in rows if r["topics"][track]["lane"] == key]
        if not subset:
            continue
        lines += [
            "", f"## {title}", "",
            "| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |",
            "| --- | --- | --- | --- | --- |",
        ]
        for row in sorted(subset, key=lambda item: item["repo"].casefold()):
            name = row["repo"]
            statuses = ["GitHub 已归档" if row["archived"] else "未标记归档", f"`{row['license']}`"]
            if row["fork"]:
                statuses.append("公开 fork")
            if read_only(row):
                statuses.append("仅作阅读参考")
            if row.get("rights_note"):
                statuses.append(row["rights_note"])
            sources = " · ".join(source_links(row))
            other_tracks = " · ".join(
                f"[{other}](../{data['topics'][other]['page']})" for other in data["topics"] if other != track and other in row["topics"]
            ) or "—"
            use = row["topics"][track]["use"].replace("|", r"\|")
            lines.append(f"| [`{name}`](https://github.com/{name}) | {use} | {'；'.join(statuses)} | {sources} | {other_tracks} |")
    lines += [
        "", "## 边界与投稿", "",
        "许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。"
        "不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。",
        "",
        f"欢迎在 [{discussion_label}]({forum}) 推荐仓库、分享使用经验或复现，也可提交 PR。"
        "请提供规范仓库 URL、领域用途、来源和权利限制；"
        "跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。",
        "",
    ]
    return "\n".join(lines)


def render_market_map(data):
    rows = data["repositories"]
    placements = sum(len(row["topics"]) for row in rows)
    cross_listed = sum(len(row["topics"]) > 1 for row in rows)
    lines = [
        "# P-Finance · 行业仓库目录", "",
        f"**{len(rows)} 个不重复公开仓库 · {placements} 个专题位置 · {cross_listed} 个跨专题仓库**",
        f"目录更新：{data['expanded_at']}（Asia/Shanghai）。", "",
        "点击行业标题展开编号清单。编号不是排名。银行合并对公、投行、FICC、托管、财富管理，"
        "在银行组内去重。同一仓库可跨组出现；各专题页面给出具体用途、固定来源和许可边界。", "",
        "[Repo 总目录](README.md) · [规范来源账本](finance-topics.json) · "
        "[收录范围与验证](../update/2026-11-20-finance-market-map.md)", "",
    ]
    for label, tracks in GROUPS.items():
        group = sorted((row for row in rows if any(track in row["topics"] for track in tracks)),
                       key=lambda row: row["repo"].casefold())
        links = " · ".join(f"[{data['topics'][track]['title']}]({PAGES[track]})" for track in tracks)
        lines += ["<details>", f"<summary>{label}（{len(group)}）</summary>", "", links, ""]
        for number, row in enumerate(group, 1):
            name = row["repo"]
            use = row["topics"][next(track for track in tracks if track in row["topics"])]["use"]
            note = " · 仅作阅读参考" if read_only(row) else ""
            lines.append(f"{number}. [`{name}`](https://github.com/{name})：{use}{note}")
        lines += ["", "</details>", ""]
    lines += [
        "这里只收录已核验的公开资料，不等于全网清单、开源合规结论或应用能力验证。"
        "未运行上游代码、未拉取商业数据、未连接实盘：**NOT_RUN / UNMEASURED**。", "",
    ]
    return "\n".join(lines)


def run(check=False):
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    validate(data)
    stale = []
    pages = {plan["page"]: render_topic(data, track) for track, plan in data["topics"].items()}
    pages[MARKET_MAP] = render_market_map(data)
    for relative, expected in pages.items():
        path = ROOT / "repo" / relative
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8", newline="\n")
    if stale:
        raise SystemExit("Regenerate finance topic pages: " + ", ".join(stale))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing anything")
    run(parser.parse_args().check)
