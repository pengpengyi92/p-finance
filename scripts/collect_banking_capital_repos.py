"""Collect public metadata and render a bounded banking/private-capital reading map."""
import argparse
import base64
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "repo" / "banking-capital"
CATEGORIES = {
    "institutions": "GS / JPMorgan / Morgan Stanley / Deutsche Bank",
    "corporate-banking": "Corporate banking / 对公、信贷、结算与现金管理",
    "investment-banking": "Investment banking / 财报、估值、资本市场与工程",
    "private-equity": "Private equity / LBO、现金流绩效与公司关系",
    "venture-capital": "Venture capital / 股权表、融资与投后数据",
}
CACHE_DIR = None
RESUME = False
OBSERVED_AT = {}


def now():
    return datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


def api(endpoint, optional=False):
    cached = CACHE_DIR / (hashlib.sha256(endpoint.encode()).hexdigest() + ".json") if CACHE_DIR else None
    if RESUME and cached is not None and cached.exists():
        record = json.loads(cached.read_text(encoding="utf-8"))
        OBSERVED_AT[endpoint] = record["observed_at"]
        return record["response"]
    for attempt in range(2):
        try:
            result = subprocess.run(
                ["gh", "api", endpoint], capture_output=True, text=True,
                encoding="utf-8", timeout=40,
            )
        except subprocess.TimeoutExpired:
            result = None
        if result is not None and result.returncode == 0:
            response = json.loads(result.stdout)
            OBSERVED_AT[endpoint] = now()
            if cached is not None:
                cached.write_text(json.dumps({"endpoint": endpoint, "observed_at": OBSERVED_AT[endpoint], "response": response}), encoding="utf-8")
            return response
        if optional and result is not None and "HTTP 404" in result.stderr:
            OBSERVED_AT[endpoint] = now()
            if cached is not None:
                cached.write_text(json.dumps({"endpoint": endpoint, "observed_at": OBSERVED_AT[endpoint], "response": None}), encoding="utf-8")
            return None
        if attempt == 0:
            time.sleep(1)
    raise RuntimeError("Public API lookup failed: " + endpoint)


def license_class(signal):
    if signal == "Community-Spec-1.0":
        return "specification-terms"
    if signal in {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "Unlicense", "ISC", "CC0-1.0"}:
        return "permissive-signal-review-text"
    if signal and signal.startswith(("GPL-", "LGPL-", "AGPL-", "MPL-", "EPL-")):
        return "reciprocal-signal-review-text"
    return "needs-license-review"


def metadata(info):
    if info["private"]:
        raise ValueError("Private repositories are outside this public catalog")
    name = info["full_name"]
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name):
        raise ValueError("Unexpected repository identifier")
    return {
        "repository": name, "url": "https://github.com/" + name,
        "description": info.get("description"), "private": False,
        "fork": info["fork"], "archived": info["archived"],
        "default_branch": info["default_branch"], "pushed_at": info["pushed_at"],
        "size_kb": info.get("size"),
        "license_signal": (info.get("license") or {}).get("spdx_id"),
    }


def collect(review_dir, resume=False):
    global CACHE_DIR, RESUME
    config = json.loads((DEST / "catalog.json").read_text(encoding="utf-8"))
    review_dir = review_dir.resolve()
    if review_dir.is_relative_to(DEST.resolve()):
        raise ValueError("Raw review material must stay outside the public catalog")
    if review_dir.is_relative_to(ROOT.resolve()) and not review_dir.is_relative_to((ROOT / ".local").resolve()):
        raise ValueError("Inside this checkout, raw review material must use ignored .local/")
    review_dir.mkdir(parents=True, exist_ok=True)
    CACHE_DIR = review_dir / "api-cache"
    CACHE_DIR.mkdir(exist_ok=True)
    RESUME = resume
    snapshot = {
        "schema_version": 1, "title": config["title"], "observed_at": now(),
        "scope": "Complete paginated public non-fork inventories of four named organizations; selected cross-ecosystem guides, not all financial software on GitHub.",
        "execution": "Third-party software and financial outcomes NOT_RUN / UNMEASURED",
        "institutions": [], "repositories": [], "reference_only": [],
        "inventory_only": config.get("inventory_only", []),
        "resumed_cached_observations": resume,
    }
    for institution in config["institutions"]:
        org = institution["organization"]
        profile = api("orgs/" + org)
        repos, fork_count = [], 0
        for page in range(1, 21):
            batch = api(f"orgs/{org}/repos?type=public&per_page=100&sort=full_name&page={page}")
            for info in batch:
                if info["fork"]:
                    fork_count += 1
                else:
                    repos.append(metadata(info))
            if len(batch) < 100:
                break
        else:
            raise RuntimeError("Inventory pagination limit reached for " + org)
        names = [row["repository"].casefold() for row in repos]
        if len(names) != len(set(names)):
            raise RuntimeError("Duplicate inventory page entries; retry snapshot for " + org)
        snapshot["institutions"].append({
            **institution, "profile_url": profile["html_url"],
            "profile_blog": profile.get("blog"), "observed_at": now(),
            "profile_observed_at": OBSERVED_AT["orgs/" + org],
            "page_observations": [
                {"page": number, "observed_at": OBSERVED_AT[f"orgs/{org}/repos?type=public&per_page=100&sort=full_name&page={number}"]}
                for number in range(1, page + 1)
            ],
            "pages_read": page, "pagination_complete": True,
            "excluded_forks": fork_count, "repositories": sorted(repos, key=lambda x: x["repository"].casefold()),
        })
        print(f"INVENTORY {org}: {len(repos)} non-forks, {fork_count} forks excluded", flush=True)
    inventory = {
        row["repository"].casefold(): row
        for org in snapshot["institutions"] for row in org["repositories"]
    }
    for item in snapshot["inventory_only"]:
        row = inventory.get(item["repository"].casefold())
        if row is None or row["size_kb"] != 0:
            raise RuntimeError("Recheck the empty-repository exclusion: " + item["repository"])
        item.update(row)
    for section in ("repositories", "reference_only"):
        for item in config[section]:
            requested = item["repository"]
            info = api("repos/" + requested)
            row = {**item, **metadata(info), "requested_repository": requested, "observed_at": OBSERVED_AT["repos/" + requested]}
            commit = api(f"repos/{row['repository']}/commits/{quote(row['default_branch'], safe='')}")
            row["head"] = commit["sha"]
            row["head_date"] = commit["commit"]["committer"]["date"]
            row["sources"] = []
            for label, endpoint in (("README", "readme"), ("LICENSE", "license")):
                blob = api(f"repos/{row['repository']}/{endpoint}?ref={row['head']}", optional=True)
                if blob is None:
                    continue
                source = {
                    "kind": label, "path": blob["path"], "blob_sha": blob["sha"],
                    "url": f"https://github.com/{row['repository']}/blob/{row['head']}/{quote(blob['path'], safe='/')}",
                    "observed_at": OBSERVED_AT[f"repos/{row['repository']}/{endpoint}?ref={row['head']}"],
                }
                if blob.get("encoding") == "base64":
                    raw = base64.b64decode(blob["content"])
                    source["sha256"] = hashlib.sha256(raw).hexdigest()
                    (review_dir / (row["repository"].replace("/", "__") + "_" + label + ".txt")).write_bytes(raw)
                row["sources"].append(source)
            row["license_class"] = license_class(row["license_signal"])
            row["validation"] = "PUBLIC_SOURCE_REVIEW_NOT_EXECUTED"
            snapshot[section].append(row)
            print(f"SOURCE {row['repository']} {row['head'][:8]} {row['license_signal']} archived={row['archived']}", flush=True)
    snapshot["completed_at"] = now()
    (DEST / "snapshot.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def cell(value):
    return str(value or "not detected").replace("|", "\\|").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;")


def source_links(row):
    return " · ".join(f"[{source['kind']}]({source['url']})" for source in row["sources"]) or "No root README/license detected"


def render():
    snapshot = json.loads((DEST / "snapshot.json").read_text(encoding="utf-8"))
    for category, title in CATEGORIES.items():
        rows = [row for row in snapshot["repositories"] if category in row["categories"]]
        lines = [f"# {title}", "", f"**Reviewed:** {snapshot['completed_at']} (Asia/Shanghai).", "",
                 "[Catalog home](README.md) · [Source snapshot](snapshot.json) · [Search boundaries](SEARCH_PROTOCOL.md)", "",
                 "Roles below are attributed explicitly. A bank-owned engineering library is not automatically an IB or corporate-banking business system.", "",
                 "| Repository / attribution | Use / reading entry | License / state / limits | Pinned primary sources |",
                 "| --- | --- | --- | --- |"]
        for row in rows:
            state = "ARCHIVED; historical only" if row["archived"] else "not archived; runtime NOT_RUN"
            note = ("<br>" + cell(row["license_note"])) if row.get("license_note") else ""
            lines.append(f"| [{row['repository']}]({row['url']})<br>{cell(row['institution'])}; `{row['relationship']}` | {cell(row['use'])} | {cell(row['license_signal'])}; {row['license_class']}; {state}<br>{cell(row['boundary'])}{note} | {source_links(row)} |")
        lines += ["", "Metadata is a dated observation. SPDX is an API classification, not legal clearance. Read the pinned license, file-level exceptions and data terms before reuse. No upstream source/data is mirrored or executed.", ""]
        (DEST / (category + ".md")).write_text("\n".join(lines), encoding="utf-8", newline="\n")
    lines = ["# Four-bank public repository inventory", "", f"**Snapshot completed:** {snapshot['completed_at']} (Asia/Shanghai).", "",
             "All public non-fork repositories returned by complete pagination of these four organizations, including general engineering and historical material. This is not a list of all bank software or all GitHub organizations affiliated with each group.", "",
             "[Curated reading routes](README.md) · [Machine-readable evidence](snapshot.json)", ""]
    for org in snapshot["institutions"]:
        lines += [f"## {org['name']}", "", f"Observed {org['observed_at']}; {len(org['repositories'])} public non-forks; {org['excluded_forks']} forks excluded; {org['pages_read']} API page(s), pagination complete.", "",
                  "| Repository | Public description | License signal | State |", "| --- | --- | --- | --- |"]
        for row in org["repositories"]:
            lines.append(f"| [{row['repository']}]({row['url']}) | {cell(row['description'])} | {cell(row['license_signal'])} | {'ARCHIVED' if row['archived'] else 'inventory only; NOT_RUN'} |")
        lines.append("")
    lines += ["## Inventory-only exclusions", ""]
    for row in snapshot["inventory_only"]:
        lines.append(f"- [{row['repository']}]({row['url']}): {cell(row['reason'])}")
    lines.append("")
    (DEST / "institution-inventory.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    lines = ["# Reference-only candidates", "", f"**Reviewed:** {snapshot['completed_at']} (Asia/Shanghai).", "",
             "Public visibility is not an open-source license. These entries are for source inspection/discovery only; do not copy, fork for reuse, install or redistribute assuming permission.", "",
             "| Candidate | Reason | Current license signal | Pinned source |", "| --- | --- | --- | --- |"]
    for row in snapshot["reference_only"]:
        lines.append(f"| [{row['repository']}]({row['url']}) | {cell(row['reason'])} | {cell(row['license_signal'])} | {source_links(row)} |")
    lines.append("")
    (DEST / "reference-only.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collect", action="store_true")
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--review-dir", type=Path)
    parser.add_argument("--resume", action="store_true", help="Reuse successful public API observations in the same local review directory; not a fresh source refresh")
    args = parser.parse_args()
    if args.collect:
        if args.review_dir is None:
            parser.error("--collect requires --review-dir for local raw-source review")
        collect(args.review_dir, args.resume)
    if args.render:
        render()
    if not args.collect and not args.render:
        parser.error("choose --collect and/or --render")
