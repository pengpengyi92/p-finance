# Corporate Finance / FICC Repo Guides

**Date:** 2026-11-14 (Asia/Shanghai). **Owner:** Pengyi Peng. Prepared with Codex assistance.

## Baseline and change

Base commit: `f5f5b10ecf3fa05d3b9c28abe4530d926675094e`.
The existing Repo section contained the LLMQuant community guide. Added8
repository cards,2 reading routes and1 reproducibility guide, with public
source pins, checked source paths, license/data limits and real contribution
states. The LLMQuant guide is byte-for-byte unchanged (Git blob
`dc76daa0c640ee060e33d246002a053d515f9383`).

- [Repo index](../repo/README.md)
- [Corporate Finance](../repo/corporate-finance/README.md)
- [FICC / curves, pricing and risk](../repo/ficc/README.md)
- [How to study](../repo/HOW_TO_STUDY.md)
- [Official-source snapshot](../repo/source_snapshot.json)

The existing application's version stays **0.3.0**. No financial models,
matching logic, credentials, data vendors, UI, API or deployment configuration
were changed. No new external PR, legal signature or outreach in this task.

## Observed public contribution status

Official GitHub reads on this date show FinanceToolkit425–429 **MERGED**;
NumPy Financial176, Strata2825/2826, FinancePy450/451, ORE377/378 and
GS Quant419/420 **OPEN**. QuantLib3046 is a **CLOSED Issue**, not our code PR.
Strata2828 is an **OPEN Issue**. rateslib1291 is an **UNANSWERED Discussion**,
not permission to modify the library. Exact URLs, authors, update/merge times
and source HEADs are in the snapshot; no upstream acceptance is inferred from
a local test, an issue closure or an unanswered question.

## Observed checks

Windows, Node24.18.0, Python3.12.14; dependency lock SHA-256
`39119aa69949fbf7df140b4afca2d687b39f9192769f13754cbdac3b7f2851ba`.
Reused existing dependencies only after lock identity comparison; no package
upgrade or fresh market-data download. Commands ran from this repository root.

| Command / check | Actual result | Scope |
| --- | --- | --- |
| `python -m unittest discover -s tests/repo_guides -v` initial | 6 pass / 1 fail, exit1 | The initial workstation-path regex incorrectly matched the tail of HTTPS; no actual private path found |
| Same command after regex fix + dedicated detector regression | **8 pass**, exit0 |8 public sources/cards, local links, >=30 pinned source links, contribution types, permissions and public-boundary checks |
| `npm run check` | **PASS**, exit0;132 tests in8 files | Schema/examples, Worker type generation, TypeScript, unit/CLI tests and Vite production build |
| `npm run test:e2e` with `CI=true` | **12 pass**, exit0 | Existing local Chromium application workflows on fresh local D1; no user browser/session reused |
| `git diff --check` | PASS | Authored changes only |

Browser tests used the repository's own local server after checking its port
was free; CI mode disabled existing-server reuse. No production deployment or
remote D1 migration was performed. Warnings about dependency PURE comments,
bundle size, color flags and locally untriggered scheduled events were observed;
they did not fail these checks. Backend Python/SQLite integration and production
browser tests were not independently rerun in this documentation task.

These are **P-Finance catalog/application checks**, not fresh executions of
FinanceToolkit, QuantLib, Strata, FinancePy, ORE, GS Quant, NumPy Financial or
rateslib financial models. Cross-library numeric comparisons, learning gain,
economic validity and speed advantages remain **NOT RUN / UNMEASURED**.
Remote CI is separate; no success is claimed before it is observed.

Source-snapshot SHA-256:
`df188a5bf1ae5fe4488703305fe624d3e3cac0d77aca141a7c8c33071d0d633f`.
The existing CI now runs the offline guide tests as a separate step; this does
not add financial-model execution or change any workflow permissions.

## Provenance and limitations

Read-only official GitHub metadata, README/license documents, Git trees and
public contribution endpoints were consulted. Context7's documentation lookup
returned a quota limit; official upstream material was used instead. No new
subscription/account or paid infrastructure was created.

Only links and metadata are published, not upstream source/license mirrors,
private research logs, raw market data or workstation paths. API license
classification is a signal, not a rights decision: QuantLib/ORE require reading
their license text, FinancePy has copyleft obligations, GS services need separate
entitlements, and rateslib is source-available rather than open source.

## Refresh and next action

`scripts/collect_repo_sources.py` refreshes the public source snapshot with
authenticated read-only `gh` requests. Its local review directory must be outside
the public checkout; review files must never be staged. Updating the JSON does
not automatically update the authored cards: reconcile changed status, paths,
permissions and dates, then run the guide tests before publishing.

Next bounded research task: one synthetic cashflow/WACC or PV/DV01 comparison,
with hand-calculated baseline, fixed conventions and negative controls, following
[the study template](../repo/HOW_TO_STUDY.md). Do not treat this plan as completed.

## Publication receipt

Guide commit `643be42f9f9daac70e67448f66fa3a731a9e296c` was pushed to P-Finance
main; authenticated Git ref readback matched exactly. Remote repo/ listing
contains both category directories, the study guide, evidence JSON and the
unchanged LLMQuant guide with the blob recorded above. This later receipt update
does not change the financial application or claim a self-referential final SHA.

At receipt time [GitHub CI](https://github.com/pengpengyi92/p-finance/actions/runs/43569985135)
was **IN PROGRESS**, not yet a remote PASS. Local checks remain as separately
recorded above. No deployment was requested or performed.
