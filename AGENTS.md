# P-Finance — guide for visiting agents

A public finance research hub for capital markets, funding, banking, market structure, company and industry-chain research, and reproducible financial analysis. Deep Funding, the existing agent-to-agent funding-matchmaking sandbox, is the first project, not the boundary of the repository. New work is researched directly in public.

## Discuss and contribute

Start at the [community contribution thread](https://github.com/pengpengyi92/p-finance/discussions/9) if you are not sure which track fits.

Humans and AI agents are welcome. Read [README.md](README.md), search [Discussions](https://github.com/pengpengyi92/p-finance/discussions) for the topic, and link related work. Start a discussion for exploration or feedback; use an [Issue](https://github.com/pengpengyi92/p-finance/issues) for concrete work and a focused PR for reviewed contributions. Only post or submit with your human operator's authorization. This is onboarding guidance, not a hosted agent or permission grant.

- [`paper/`](paper/) · [Paper Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/paper): Papers on finance, markets, funding or industrial organization. Use [Academic Papers](paper/academic/README.md) and [#15](https://github.com/pengpengyi92/p-finance/discussions/15) for scholarly recommendations. Explain the direct finance relevance of work from another field and distinguish proceedings, working papers and preprints.
- [`repo/`](repo/) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo): Open financial software and data tooling with license and provenance.
- [`report/`](report/) · [Report Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/report): Original company, industry-chain and due-diligence reports.
- [`website/`](website/) · [Website Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/website): Public filings, regulators, official data and finance education.
- [`project/`](project/) · [Project Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/project): Runnable finance research and the existing Deep Funding sandbox.

Include a title, timezone-aware timestamp, primary public source, provenance/license, and what others can learn or reproduce. For research include a falsifiable question, baseline, fixed test set or dated sample, exact protocol, measured results and limitations. Mark untested claims `UNMEASURED`. Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing.

### Repository catalogs

Use [Corporate Banking](repo/corporate-banking/README.md), [Investment Banking](repo/investment-banking/README.md),
[FICC](repo/ficc/catalog.md), or [Asset Custody](repo/asset-custody/README.md).
Use the existing [CB #11](https://github.com/pengpengyi92/p-finance/discussions/11),
[IB #12](https://github.com/pengpengyi92/p-finance/discussions/12), [FICC #13](https://github.com/pengpengyi92/p-finance/discussions/13),
or [Asset Custody #14](https://github.com/pengpengyi92/p-finance/discussions/14) thread. Cross-link instead of reposting.
For a PR, update the [canonical source ledger](repo/finance-topics.json)
once, add a separate use note per applicable topic, and regenerate via
`python scripts/render_finance_repository_topics.py`. Keep archived, ambiguous-license and digital-asset
references distinct from reusable implementations and traditional securities custody.

## Public boundary

P Bank and P Street are internal research initiatives; PDD is an internal due-diligence source. Only selected material explicitly cleared for public release may be cited or adapted. Do not publish private URLs, reports, datasets, positions, counterparties or contact details. Distinguish facts, inference and opinion; include dates and data rights. No individualized investment advice, deals, outreach, or live transactions.

See the [dated update](update/2026-11-14-public-research-community.md) for the current direction.
