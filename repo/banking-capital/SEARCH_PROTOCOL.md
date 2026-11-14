# Search protocol and completeness limits

**Research date:** 2026-11-15, Asia/Shanghai. Exact collection times: [snapshot](snapshot.json).

## Question and scope

Which public repositories help study corporate banking, investment banking, PE and VC,
and which are actually bank-owned rather than foundation or community projects?
No source or investment-quality score is inferred from brand or star count.

- Enumerate `goldmansachs`, `jpmorganchase`, `morganstanley`, and `deutschebank` with
  `GET /orgs/{org}/repos?type=public&per_page=100&sort=full_name&page=N` until the
  final short page. Exclude forks but retain their count. Keep all public non-forks,
  including archived and generic engineering repositories, in the inventory.
- This is exhaustive only for those four named organizations at observation time.
  It excludes private repositories, affiliated organizations not enumerated, other Git
  hosts, undisclosed internal systems, and unlicensed/proprietary bank/fund software.
- Extend selected routes using the existing P-Finance public guides, FINOS/Apache/
  Open Cap Table Coalition primary repositories, official README/organization pages,
  and bounded GitHub searches for `leveraged-buyout`, `private-equity`, `venture-capital`,
  `Open-Cap-Format`, and `YC Open API`. Search is discovery, not verified attribution;
  the PE/VC cross-ecosystem selection is not exhaustive. The last query found no result.
- A Morgan Stanley GraphQL inventory request and some discovery requests timed out.
  The final bank inventory uses successfully completed REST pagination, not the failed
  response. Transient failures are not interpreted as absence of a repository.

## Source pinning and rights

For every selected/reference-only entry, resolve the canonical repository, read public
metadata, pin the default-branch commit, and resolve root README/license content at that
commit. Publish source paths, Git blob IDs and content SHA-256 where supplied. Do not
mirror source code, redistribute datasets or run upstream install scripts. Missing root
license discovery means `needs-license-review`, not legal clearance or proof of no rights.

Primary README/license links are pinned; institution homepages are provenance pointers
and may redirect or be unavailable. Link availability does not establish financial
correctness, continued maintenance, entitlement, production security, or legal approval.
The repository listing is not an atomic multi-organization snapshot; timestamps make that
limitation visible. Re-run collection if pagination duplicates or missing API data occur.

## Measurement

Baseline: the existing public company-finance/FICC guides and institution selection.
Change: a complete four-organization non-fork inventory plus multi-label business routes.
Fixed tests verify pagination receipts, public-only scope, unique canonical identities,
source pins, timezone-aware timestamps, rights classifications, local links and negative
controls for private/unclear-license material. Existing guide contracts remain enforced.

Catalog consistency can be measured. Financial model quality, costs, operational utility,
runtime safety, learner improvement and return forecasts are **UNMEASURED**. No cross-library
pricing or bank production benchmark is claimed. See the dated report for actual commands,
counts, failures and remaining milestones.
