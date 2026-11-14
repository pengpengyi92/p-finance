# Banking / IB / PE / VC：公开仓库调查与学习路线

**Title:** P-Finance banking and private-capital repository expansion.
**Date:** 2026-11-15, Asia/Shanghai. 每条 API 观察时间及固定源文件见
[来源快照](../repo/banking-capital/snapshot.json)。
**Source snapshot completed:** `2026-11-15T00:36:38+08:00`; resumed reads preserve
their original API observation times rather than claiming a fresh remote fetch.
**Status:** Public-source research and cataloging; third-party runtime and financial utility
are **NOT_RUN / UNMEASURED**. This is not investment, credit or legal advice.

## 1. 本轮交付与范围

- 四个明确指定的官方 GitHub 组织，完整分页收录其公开非 fork 仓库：
  Goldman Sachs24、JPMorgan Chase65、Morgan Stanley49、Deutsche Bank5，共143个。
  另有80个 fork 被排除；不是说这些机构仅有143个软件系统。
- 45个精选项目，按机构、对公、投行、PE、VC 多标签分类；同一个项目可以服务多条路线，
  不按分类重复计数。逐条提供固定 commit、README/许可入口、用途、权利与使用边界。
- 两个未检测到许可的 PE 学习候选放入 reference-only，而非可自由复用的安装清单。
  德银空的 dbcore 只保留在全量组织目录，不计为可读实现。
- 原有8篇公司金融/FICC 详细卡、21条机构/腾讯来源记录、LLMQuant 导读和应用原样保留。
  它们与新目录存在重叠，不能简单把8、21、45相加。

入口：[仓库地图](../repo/banking-capital/README.md) ·
[四家组织完整目录](../repo/banking-capital/institution-inventory.md) ·
[原始选题与边界](../repo/banking-capital/catalog.json) ·
[采集方法与局限](../repo/banking-capital/SEARCH_PROTOCOL.md)。

“全量”严格限定于本轮枚举的四个组织、公开非 fork、观察时点；不覆盖集团其他组织、
私有库、其他 Git 托管平台或全世界所有 PE/VC 项目。跨生态精选不是穷尽性检索。

## 2. 四家机构到底开放了什么

### Goldman Sachs

GS Quant 提供量化金融接口，不能把它说成 GS 的全部投行系统。Reladomo、Obevo、jDMN
分别提供数据访问、数据库部署和业务决策逻辑等工程参考。DocKnight 的公开目标是文档
结构/视觉表达与知识抽取，README 也承认输出可能缺失或误分；它不是可信财务事实库。
Legend 已位于 FINOS，读总入口、Engine、Studio 三层时要保留当前归属与起源的区别。

### JPMorgan Chase

Fusion / Java SDK / notebooks 与 DataQuery 是不同的数据工作流。开源 SDK 不授予账户、
数据订阅或定价服务权益。Fusion 的 API 许可分类为 `NOASSERTION`，但固定 LICENSE 的
标题/声明指向 Apache2.0；不能把分类失败误写成“完全没有许可”，也不能据此忽略数据条款。

ABIDES 是市场模拟研究，不是并购或杠杆收购模型。SFinX 处理指标、期间与数值型 Excel
表格的标准化，已归档；不应被宣传成通用 LLM 尽调系统。Python training 是学习材料，
PADL 是隐私/可审计账本研究，都不等于银行的生产业务代码。

### Morgan Stanley

Optimus Cirrus 值得研究高性能依赖计算和工程组织；但 README 仍记录构建工具引导工作，
本轮没有证明它能独立构建。ComposeUI / desktopJS 是桌面/容器集成，testplan 是测试，
API 仓库是示例入口。pyfixmsg 是主要面向测试的 FIX 消息工具，已归档，不是完整交易网关。
不要把这些仓库合称“MS 的完整交易或风控模型”。

### Deutsche Bank

API Program 是开放银行开发/沙盒入口。dbMango 是带角色和审计的 MongoDB 管理工具；
README 明确一个包含德银专有数据的插件并未公开，目录不采集该插件。dbMango 的 README
有 Apache-2.0 声明，仍应读原文而不是只依赖 API 的 `NOASSERTION`。

`dbcore` 的元数据 size0，直接读 `commits/master` 返回 `HTTP409: Git Repository is empty`。
因此本轮不把名称解释成核心银行开源实现。Plexus 是德银起源、FINOS 归档的历史桌面
互操作项目，不是完整 Autobahn 定价系统；Waltz 用于企业架构/数据依赖。

各机构事实及版本入口集中在 [机构精选表](../repo/banking-capital/institutions.md)，
每行链接到本轮固定的原始 README 与许可，而不是凭品牌或星数推断用途。

## 3. 按业务研究，而不是按公司名堆链接

| 方向 | 研究链路与候选 | 必须另外验证的内容 |
| --- | --- | --- |
| 对公信贷 | 财报/现金流输入 → 显式决策规则 → 贷款与还款生命周期；FinanceToolkit、EdgarTools、jDMN、Fineract | 会计口径、发布时间、担保/抵押、审批权限、违约和回收假设；不是银行现行授信政策 |
| 结算/现金管理 | ACH / wire / SWIFT MT 的格式、校验、审计；Moov、Prowide | 地区/标准版本、清算资格、网络及账户权限；格式通过不代表付款成功 |
| 对公数据治理 | 客户/产品/交易口径、来源和应用依赖；Legend、Waltz、Reladomo | 主数据、历史版本、访问控制、客户保密与监管边界 |
| 投行研究 | 财报输入 → 比率/现金流 → 估值/情景；EdgarTools、FinanceToolkit、numpy-financial | 三表勾稽、股数/币种/单位、发布与修订时间、银行与工业公司估值差异 |
| 资本市场工程 | 产品/生命周期标准 → 数据接入 → 风险/展示；CDM、GS Quant、Fusion/DataQuery、Perspective、FDC3 | 许可、订阅、产品覆盖、时点一致性；不是 M&A 执行或承销权限 |
| PE | 买入估值/融资 → 债务偿还 → 退出 → IRR/MOIC/PME；LBO 教学、PyXIRR、CompanyKG | 费用/税、杠杆、现金流符号、NAV、基准时间、损失情景；个人示例不代表基金模型 |
| VC | 股权数据/期权/融资轮次 → 稀释 → 交换/投后分析；OCF、OCX、Captable | 清算优先权、转股、期权池、日期、法律效力；数据 schema 不等于完整分配瀑布引擎 |

结算路线还要区分历史协议和当前项目：`moov-io/wire` 是归档的 FAIM 历史工具；
`moov-io/wire20022` 的项目说明也标为 deprecated，指向本轮补入的
`moov-io/fedwire20022`。后者 README 说明只覆盖部分 Fedwire ISO20022 消息，并提示
早期阶段及 XML namespace 局限；不能把迁移后的新仓库自动称为生产就绪。
协议迁移背景见[美联储官方实施中心](https://www.frbservices.org/resources/financial-services/wires/fedwire-funds-service-iso-20022-implementation-center/)，
项目边界和版本见[对公导读的固定原文](../repo/banking-capital/corporate-banking.md)。

贸易融资、保函、信用证、供应链资产、完整并购/承销流程以及基金 LP 税务和运营，本轮
没有验证一个通用、生产可用的开源实现。不能拿支付格式库或学习模型填补这些空白；这也
不是证明相应开源项目不存在，只是当前证据未覆盖。

## 4. 值得先做的六个小项目

下列是下一阶段建议，不是本轮执行结果或质量排名。只用自造/授权数据。

1. **对公贷款闭环**：用 Fineract 的领域对象研究本金、利息、还款、逾期状态；独立验证
   还款计划与本金余额守恒，并加入错误日期/金额/权限的负对照。
2. **支付文件验证**：选一种 ACH 文件，构造合法合成样例及错误 routing checksum、
   不平衡批次、缺失字段；验证拒绝行为。禁止向银行发真实付款。
3. **财报输入与时点**：读授权的 issuer/SEC 文件，保留发布时间、修订版本和原始单位；
   三表不勾稽/未来文件必须拒绝。不要把下载成功等同财务事实正确。
4. **PE 现金流与绩效**：先手算，再对照 PyXIRR。固定数据可用投入100、已分配20、
   期末 NAV110，理论 `DPI=0.2, RVPI=1.1, TVPI=0.2+1.1=1.3`；这是未运行的算术 oracle，
   不是基金业绩。再加入零投入、负 NAV、不同计价日期和多根 IRR 案例。
5. **LBO 的三层核对**：教学模型的资金来源/用途、每期债务与现金、退出桥与收益率分别
   勾稽；以独立 Excel 或简单现金流程序为 baseline，不调参数制造更高回报。
6. **VC 股权数据闭环**：合成 OCF → OCX/Excel → 明确的股数/稀释核对；加重复交易、
   错误生效日期、期权池计数和负股数的负对照。真实股东数据不进入公共仓库。

## 5. 工程交付和测量

本轮新增来源采集与可再生成导读脚本、离线契约测试；保留既有8库/21来源断言，扩展而非
绕过新 pin 的验证。测试覆盖完整分页记录、canonical repo 去重、固定 commit/源文件、
时区时间戳、归属、许可负对照、公开/私有隔离和本地链接。应用、引擎及依赖版本不改。

实际命令、测试数量与失败记录已在 [检查回执](../repo/banking-capital/CHECKS.json) 和
[工作日志](../log/2026-11-15-banking-private-capital-repositories.md) 留存。
采集器首次在空 dbcore 的 commit 查询停止；没有把错误变成可用源码。修订后将该条
保留在组织 inventory，并支持显式恢复成功的公开 API 观察，避免反复浪费请求。
恢复缓存保留原观察时间，不冒充重新从远端获取。

评估只针对目录一致性与工程回归。第三方程序执行、金融数值等价、投资效用、学习收益、
生产部署安全性、授权数据覆盖及真实投资表现：**UNMEASURED**。

本地最终验证：21项目录测试、132项既有单元/CLI测试、类型/构建检查以及12项浏览器
回归通过。首次 `npm run check` 在缺少 Windows workerd 可选二进制处停止，之后恢复
包含可选依赖的精确锁定树，未改 package.json/package-lock.json。锁文件依赖审计仍显示
10项告警（含2项 critical），未在目录任务中强制升级或部署；这不是生产安全验收。
后端 Python/SQLite 集成未在本轮独立重跑。

## 6. 权利与持续更新

AGPL 的网络服务相关义务、规范与实现的不同许可、文件级例外、第三方依赖和外部数据
都需逐项检查。开放源代码不等于开放数据、免费商业 API 或无条件 SaaS 再分发权限。
归档仓库保留历史学习价值，但不是当前维护承诺。

OCF 是很好的具体例子：固定 Schema and Documentation License1.0.1 对规范文件适用
专门条款，允许带通知的实现所需派生，但禁止将派生文件当作技术规范发布；Code
Components（示例及编程代码等）另适用 Apache2.0。不能只看到“公共格式”或 GitHub
`NOASSERTION` 就认定整个仓库统一没有许可、或统一可以任意修改/分发。

本轮没有联系银行/基金、提出新 PR、投稿 Discussion、注册金融产品、获取客户资料、
调用交易/支付接口或部署新服务。下一阶段先选一个最小合成案例，单独写 benchmark card，
再判断是否值得工程接入。目录链接本身不是完成接入的证据。
