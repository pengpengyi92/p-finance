"""Render the four public repository research topics from one reviewed source ledger."""

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
PAGES = {
    "CB": "corporate-banking/README.md",
    "IB": "investment-banking/README.md",
    "FICC": "ficc/catalog.md",
    "AC": "asset-custody/README.md",
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
    if data["schema_version"] != 1 or datetime.fromisoformat(data["observed_at"]).utcoffset() != timedelta(hours=8):
        raise ValueError("A versioned UTC+08:00 snapshot is required")
    names = set()
    plans = data["topics"]
    if {track: plan["page"] for track, plan in plans.items()} != PAGES:
        raise ValueError("Expected exactly four finance topics")
    discussion_numbers = [plan.get("discussion") for plan in plans.values()]
    if any(type(number) is not int or number < 1 for number in discussion_numbers) or len(set(discussion_numbers)) != len(PAGES):
        raise ValueError("Each topic requires a distinct public discussion number")
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
        if not row["topics"]:
            raise ValueError(f"Missing topic for {full}")
        for track, note in row["topics"].items():
            if note["lane"] not in plans[track]["lanes"] or not note["use"].strip() or "\n" in note["use"]:
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
    scope = ", ".join(data["topics"][t]["title"].split(" / ")[0] for t in data["topics"] if t != track)
    lines = [
        f"# {plan['title']}",
        "",
        f"**核对时间：** {data['observed_at']}（Asia/Shanghai） · **本专题：** {len(rows)} 个公开仓库。",
        "",
        plan["intro"],
        "",
        "[Repo 总目录](../README.md) · [公开来源账本](../finance-topics.json) · "
        f"[本专题讨论 #{plan['discussion']}]({FORUM}/{plan['discussion']}) · "
        f"[Repo Discussions]({FORUM}/categories/repo)",
        "",
        "这是当前已核验候选的收录，不是全球全集或生产背书。"
        f"同一仓库也可能出现在 {scope}；每页写的是该用途。",
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
        f"欢迎在 [本专题讨论]({FORUM}/{plan['discussion']}) 推荐仓库、分享使用经验或复现，也可提交 PR。"
        "请提供规范仓库 URL、领域用途、来源和权利限制；"
        "跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。",
        "",
    ]
    return "\n".join(lines)


def run(check=False):
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    validate(data)
    stale = []
    for track, plan in data["topics"].items():
        path = ROOT / "repo" / plan["page"]
        expected = render_topic(data, track)
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
