# Banking & Private Capital · 银行与私募资本仓库地图

**Title:** GS / JPMorgan / Morgan Stanley / Deutsche Bank + Corporate Banking / IB / PE / VC.
**Review date:** 2026-11-15, Asia/Shanghai; exact timezone-aware timestamps and pins are in
[snapshot.json](snapshot.json). This is a public-source catalog, not a claim to have run
these systems or obtained bank/private-fund business code.

## Two layers / 两层收录

1. [四家银行完整公开非 fork 仓库快照](institution-inventory.md)：完整分页获取指定四个
   GitHub organization 的公开非 fork 仓库，含通用工程、历史项目。不是所有关联组织的全集，
   也不是银行全部业务系统的全集。未精选条目只完成目录级核对。
2. [机构精选导读](institutions.md)及以下工作流路线：逐条固定 commit、README、许可入口、
   维护/归档状态、实际用途和边界。代码没有镜像；模型没有在本轮运行。

| Route | Read for | Important distinction |
| --- | --- | --- |
| [Corporate banking / 对公](corporate-banking.md) | 信贷生命周期、决策规则、数据治理、支付报文、现金管理底座 | 通用规则/消息库不等于银行授信政策或生产清算能力 |
| [Investment banking / 投行与资本市场](investment-banking.md) | 财报输入、估值与风险、数据 SDK、前台桌面与工程 | 市场交易工具不等于 M&A/LBO 模型；SDK 不等于免费市场数据 |
| [Private equity / PE](private-equity.md) | LBO 教学、IRR/XIRR/PME、公司图谱、股权数据 | 公开教学模型不等于 PE 机构内部 IC、交易、估值或 LP 数据 |
| [Venture capital / VC](venture-capital.md) | 股权表、融资数据标准、Excel 交换、融资材料与投后分析 | 标准/自托管应用不等于基金真实资产或募资成功率 |
| [Reference-only / 权利待确认](reference-only.md) | 发现有价值但许可未确认的公开材料 | 公开可见不构成自由复用、分发或商用授权 |

## Start small / 首选研究入口

- 对公：`apache/fineract` 看贷款对象和还款生命周期；`moov-io/ach` 看可验证的支付文件；
  `finos/waltz` / `finos/legend` 看企业数据依赖和一致口径。
- 投行：已有 [公司金融导读](../corporate-finance/README.md) + `dgunning/edgartools`
  研究财报输入；已有 [FICC 导读](../ficc/README.md) + GS Quant 研究资本市场工具。
- PE：`Anexen/pyxirr` 的现金流/绩效接口 + `Nachidoestech/lbo-model` 教学案例，随后用
  独立 Excel/手算、会计恒等式、坏情景和时间戳检查复现。
- VC：先读 OCF schema，再看 OCX 的 Excel 映射和 Captable；只用合成股东、期权和融资轮次。
- 研究终端：Perspective 当前规范仓库是 `perspective-dev/perspective`；旧地址可能重定向。

这些是阅读顺序建议，不是运行结果或软件质量排名。全部业务效用、数值准确性、投资结果、
性能、部署安全性和真实数据适配均为 **UNMEASURED / NOT_RUN**。

## Ownership and rights / 归属与许可

`bank-owned` 表示当前位于对应银行组织；`foundation-project` / `community-standard`
不是银行独占项目；`pe-firm-owned` 与社区/个人教学项目分别标注。官方归属不自动证明
该项目由某个 Corporate Banking、IB、PE 或 VC desk 维护。

许可列是 GitHub 的 SPDX 识别信号，必须读固定版本原文和文件级例外。`NOASSERTION`、
未检测到许可、自定义许可均需要额外核查；不能据此标成自由开源。AGPL 有网络服务相关义务；
规范文本、库代码、第三方数据、服务订阅和商标可能适用不同条款。

原始 README/许可仅在忽略的本地审阅目录保存；公开目录只包含链接、元数据和原创摘要。
不发布内部报告、客户资料、账户配置、数据包、真实投资人联系人或交易指令。

## Refresh / 可复现更新

```sh
python scripts/collect_banking_capital_repos.py --collect --render --review-dir .local/banking-review
python -m unittest discover -s tests/repo_guides -v
```

从仓库根目录运行，需要已认证的 `gh` 仅用于读取公开 API。采集不会发 issue/PR/comment、
执行第三方代码、创建金融账户、申请产品权限或交易。[搜索边界与方法](SEARCH_PROTOCOL.md) ·
[总报告](../../report/2026-11-15-banking-private-capital-repositories.md) ·
[已有 FICC 机构导读](../ficc-institutions.md) · [全部仓库入口](../README.md) ·
[可编辑选题/边界](catalog.json)。

[本地测试与哈希回执](CHECKS.json) ·
[交付与远端核对](../../update/2026-11-15-banking-private-capital-repositories.md)。
