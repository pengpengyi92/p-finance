# P-Finance · Repo

Open financial software and data tooling with license and provenance.

**Latest catalog:** 2026-11-18 (Asia/Shanghai). 四个公开仓库专题按业务用途组织；下方早期报告和原始来源快照继续保留。

## 四个独立专题

| 专题 | 收录范围 |
| --- | --- |
| [Corporate Banking / 对公银行](corporate-banking/README.md) | 公司信贷、支付、银企直联、现金管理与贸易融资 |
| [Investment Banking / 投资银行](investment-banking/README.md) | 财报、估值、并购、杠杆收购、股债融资与市场工程 |
| [FICC / 固收、外汇与商品](ficc/catalog.md) | 利率曲线、债券、信用、FX、商品和市场数据、回购与抵押品 |
| [Asset Custody / 资产托管](asset-custody/README.md) | 传统证券交收、持仓、对账、公司行动；分列代币化与数字资产工具 |

同一项目可以出现在多个专题，分别解释其用途；[规范来源账本](finance-topics.json)只登记一次。
[范围与核对方式](../update/2026-11-18-four-repository-topics.md) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)。

## Start here / 从这里开始

- [Banking / IB / PE / VC](banking-capital/README.md)：四家指定银行143个公开非 fork
  仓库的完整分页快照、45个精选项目与对公/投行/私募资本路线；许可不明与空仓库单独处理。
  [调查报告](../report/2026-11-15-banking-private-capital-repositories.md) ·
  [机构完整目录](banking-capital/institution-inventory.md)。本轮日期2026-11-15，原有下列卡片
  保留2026-11-14的历史来源快照，不混成同一批验证。
- [Corporate Finance](corporate-finance/README.md)：现金流 → NPV/IRR → WACC → PVGO / 增长 / 财报接口。
- [FICC](ficc/README.md)：曲线 → 债券/衍生品 → 敏感度 → 组合风险 → 数据与服务权限。
- [How to study a repo](HOW_TO_STUDY.md)：固定问题、源码入口、synthetic 小案例、证据记录和贡献边界。

| Repo 档案 | 主要用途 | 许可／重要边界 |
| --- | --- | --- |
| [FinanceToolkit](corporate-finance/finance-toolkit.md) | 公司金融、财务比率、估值/信用模型 | MIT；数据权利另行核对 |
| [NumPy Financial](corporate-finance/numpy-financial.md) | NPV、IRR 与资金时间价值 | BSD-3-Clause；周期/多根约定 |
| [FinancePy](ficc/financepy.md) | Python 曲线、债券与衍生品 | GPL-3.0-or-later；复用/分发义务 |
| [QuantLib](ficc/quantlib.md) | C++ 曲线、日期与定价基础 | QuantLib BSD 风格许可；读原文 |
| [Strata](ficc/strata.md) | Java 产品/市场/风险分层 | Apache-2.0 |
| [ORE](ficc/ore.md) | 组合、曲线配置、情景与风险 | 上游 BSD 风格文本；依赖另查 |
| [GS Quant](ficc/gs-quant.md) | 金融 SDK、数据与 pricing context | Apache-2.0 不等于 GS 数据/服务授权 |
| [rateslib](ficc/rateslib.md) | 利率研究的权限先行参考 | **Source-available, not open source**；不自动安装/fork/修改 |

每篇档案包括用途、已核对的源码/文档入口、未执行练习、公开 PR/Issue/Discussion 与限制。FinanceToolkit #425–#429 已核实 MERGED；其他状态逐条记录，不能把提交等同接受。

来源：[timestamped source snapshot](source_snapshot.json)。本轮核对官方公开元数据、README、许可及贡献状态；未安装/运行这八个库或重做历史金融实验。GitHub 许可信号不代替许可原文，代码许可不授予数据权利。

## Other repository communities

- [FICC institution and Tencent repository guide](ficc-institutions.md) — State Street, XTX, Deutsche Bank, other institutions, and the previous WeChat Pay contributions.
- [LLMQuant community and repository guide](llmquant.md) — the complete public inventory with access notes, suggested starting points, and how to contribute. [Discuss LLMQuant (#10)](https://github.com/pengpengyi92/p-finance/discussions/10).

Propose an entry in [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) or submit a focused PR. Include a title, timestamp with timezone, primary public source or synthetic fixture, rights, and one concrete reason it is useful. See [AGENTS.md](../AGENTS.md).
