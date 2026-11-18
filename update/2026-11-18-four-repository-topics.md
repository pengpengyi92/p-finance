# Four public repository topics: Corporate Banking, IB, FICC and Asset Custody

**Timestamp:** 2026-11-18T23:44:34+08:00 (Asia/Shanghai).

| Topic | Public repository placements |
| --- | ---: |
| [Corporate Banking](../repo/corporate-banking/README.md) | 53 |
| [Investment Banking](../repo/investment-banking/README.md) | 48 |
| [FICC](../repo/ficc/catalog.md) | 50 |
| [Asset Custody](../repo/asset-custody/README.md) | 33 |

**137 distinct public repositories, 184 topic placements, 36 cross-listed repositories.**
Each repository has one canonical record in [the source ledger](../repo/finance-topics.json).
The topic pages give it a different business use when it crosses a boundary. The 40
earlier Corporate Banking / IB entries are still covered; the four-bank historical
inventory, PE/VC routes, FICC reading cards, and LLMQuant guide remain in place.

## Search scope and inclusion

Started from the existing public P-Finance [banking survey](../repo/banking-capital/README.md),
[FICC institution index](../repo/ficc-institutions.md) and project discovery notes,
then independently checked public upstreams. Targeted searches included:

- Corporate banking: ACH, Fedwire, SEPA, CAMT/MT940, EBICS, MSME lending, ledger, cash reconciliation, documentary credit and credit approval.
- Investment banking: SEC filings/XBRL, DCF and WACC, deal comps, M&A/LBO, cap-table dilution, bond issuance and structured finance.
- FICC: curves, government and credit instruments, FX forwards, CTD and repo, derivatives pricing, market data interfaces, commodity curves and ETRM.
- Asset custody: securities settlement and SWIFT MT/MX, custody and reference-data standards, cash/securities reconciliation, audit trail, asset servicing, DvP and tokenization prototypes.

Checked canonical owner/repo, visibility, empty/archived/fork metadata, default branch
commit and the matching public tree for README and license paths where present.
GitHub's detected SPDX value is a signal only; archived, unclear, and separately
restricted material is labeled for reading. Resolved redirects are not counted twice
(for example OpenBB and Marker); confirmed FinancePy under the current organization.
Unpinned or unresolved candidates are recorded separately and not counted.
Nine included repositories are archived; their topic listings are historical.
The scope is this verified public candidate set, not a global inventory or a survey of
complete in-house systems. Official business/standards pages are linked as context,
not counted as software. No private links, data, source dumps, or API credentials are included.

## Verify and extend

From the P-Finance root:

```sh
python scripts/render_finance_repository_topics.py --check
python -m unittest discover -s tests/repo_guides -v
```

The renderer check and all 27 offline catalog tests passed, including both
historical source ledgers. The application's existing `npm run check` passed
(132 unit/CLI checks, schema/examples, type checking and build). The first browser
run stopped during Wrangler's local test server startup, before running any cases.

Update the ledger first and rerender. Contributions go through the existing
[Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)
or a focused PR. Reusable code, standards text, subscription data and operational
rights are separate. No upstream runtime, numeric valuation, live bank/custody
connection, production suitability or economic outcome was evaluated in this catalog
pass: **NOT_RUN / UNMEASURED**.
