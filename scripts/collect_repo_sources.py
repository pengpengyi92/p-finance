"""Read-only official-source snapshots for the public finance reading guide."""
import argparse
import base64
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
REPOSITORIES = [
    "JerBouma/FinanceToolkit", "numpy/numpy-financial", "lballabio/QuantLib",
    "tradingtechnologies/Strata", "domokane/FinancePy", "OpenSourceRisk/Engine",
    "goldmansachs/gs-quant", "attack68/rateslib",
]
CONTRIBUTIONS = {
    "JerBouma/FinanceToolkit": [("pulls", n) for n in (425, 426, 427, 428, 429)],
    "numpy/numpy-financial": [("pulls", 176)],
    "lballabio/QuantLib": [("issues", 3046)],
    "tradingtechnologies/Strata": [("pulls", 2825), ("pulls", 2826), ("issues", 2828)],
    "domokane/FinancePy": [("pulls", 450), ("pulls", 451)],
    "OpenSourceRisk/Engine": [("pulls", 377), ("pulls", 378)],
    "goldmansachs/gs-quant": [("pulls", 419), ("pulls", 420)],
    "attack68/rateslib": [],
}
INTERESTING = ("readme", "contribut", "licen", "wacc", "growth_model", "financial.py",
               "ratehelper", "bond.cpp", "zerocurve", "discountcurve", "bond_future",
               "discount_curve", "pricing_context", "fred", "zerorate", "curveconfig",
               "smithwilson", "normalformularepository", "blackformularepository")


def api(endpoint, optional=False, query=None):
    for attempt in range(3):
        command = ["gh", "api", endpoint]
        if query is not None:
            command += ["-f", "query=" + query]
        r = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        if r.returncode == 0:
            return json.loads(r.stdout)
        if optional and "404" in r.stderr:
            return None
        if attempt < 2:
            time.sleep(attempt + 1)
    raise RuntimeError(f"GET {endpoint}: {r.stderr[:200]}")


def collect(review_dir):
    review_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for name in REPOSITORIES:
        info = api("repos/" + name)
        if info["private"]:
            raise RuntimeError("Public guide cannot ingest private repository: " + name)
        commit = api(f"repos/{name}/commits/{info['default_branch']}")
        sha = commit["sha"]
        tree = api(f"repos/{name}/git/trees/{commit['commit']['tree']['sha']}?recursive=1")
        paths = [x["path"] for x in tree["tree"] if x["type"] == "blob"]
        readme = api(f"repos/{name}/readme?ref={sha}", optional=True)
        license_data = api(f"repos/{name}/license?ref={sha}", optional=True)
        for label, blob in (("README", readme), ("LICENSE", license_data)):
            if blob and blob.get("encoding") == "base64":
                (review_dir / (name.replace("/", "__") + "_" + label + ".txt")).write_bytes(base64.b64decode(blob["content"]))
        row = {"repository": info["full_name"], "url": info["html_url"], "private": info["private"],
               "archived": info["archived"], "default_branch": info["default_branch"], "head": sha,
               "observed_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
               "observed_at_utc": datetime.now(timezone.utc).isoformat(),
               "license_signal": (info.get("license") or {}).get("spdx_id"),
               "license_path": license_data.get("path") if license_data else None,
               "readme_path": readme.get("path") if readme else None,
               "tree_truncated": tree.get("truncated", False),
               "source_paths": [p for p in paths if any(x in p.lower() for x in INTERESTING)],
               "contributions": []}
        for kind, number in CONTRIBUTIONS[name]:
            pr = api(f"repos/{name}/{kind}/{number}")
            row["contributions"].append({"type": "PR" if kind == "pulls" else "ISSUE", "number": number,
                "url": pr["html_url"], "title": pr["title"], "author": pr["user"]["login"],
                "state": "MERGED" if pr.get("merged_at") else pr["state"].upper(),
                "merged_at": pr.get("merged_at"), "updated_at": pr["updated_at"]})
        if name == "attack68/rateslib":
            q = 'query { repository(owner:"attack68",name:"rateslib") { discussion(number:1291) { url title isAnswered updatedAt author { login } } } }'
            discussion = api("graphql", query=q)["data"]["repository"]["discussion"]
            row["contributions"].append({"type": "DISCUSSION", "number": 1291,
                "url": discussion["url"], "title": discussion["title"],
                "author": discussion["author"]["login"],
                "state": "ANSWERED" if discussion["isAnswered"] else "UNANSWERED",
                "updated_at": discussion["updatedAt"]})
        rows.append(row)
        print(name, sha[:8], row["license_signal"], "contributions", [(x["number"], x["state"]) for x in row["contributions"]], flush=True)
    output = ROOT / "repo" / "source_snapshot.json"
    output.write_text(json.dumps({"schema_version": 1, "scope": "Public metadata and source paths only; no code/data mirror or execution result.", "repositories": rows}, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Wrote", output, flush=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--review-dir", type=Path, required=True, help="Local review area outside public checkout")
    collect(p.parse_args().review_dir)
