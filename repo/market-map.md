# P-Finance · 行业仓库目录

**190 个不重复公开仓库 · 302 个专题位置 · 70 个跨专题仓库**
目录更新：2026-11-20T00:43:00+08:00（Asia/Shanghai）。

点击行业标题展开编号清单。编号不是排名。银行合并对公、投行、FICC、托管、财富管理，在银行组内去重。同一仓库可跨组出现；各专题页面给出具体用途、固定来源和许可边界。

[Repo 总目录](README.md) · [规范来源账本](finance-topics.json) · [收录范围与验证](../update/2026-11-20-finance-market-map.md)

<details>
<summary>Bank / 银行（144）</summary>

[Corporate Banking / 对公银行](corporate-banking/README.md) · [Investment Banking / 投资银行](investment-banking/README.md) · [FICC / 固定收益、外汇与商品](ficc/catalog.md) · [Asset Custody / 资产托管与证券服务](asset-custody/README.md) · [Wealth Management / 财富管理](wealth-management/README.md)

1. [`actualbudget/actual`](https://github.com/actualbudget/actual)：本地优先的信封预算与家庭现金流规划；银行同步权限需独立获得
2. [`alpacahq/alpaca-py`](https://github.com/alpacahq/alpaca-py)：券商 SDK 可读账户/持仓/活动；非证券托管实现，不连接账户
3. [`Amitav507/energy-derivatives-pricing`](https://github.com/Amitav507/energy-derivatives-pricing)：能源衍生品 Black-76、Bachelier 与蒙特卡洛练习；未独立校验
4. [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr)：不规则日期收益率与 PE 绩效分析函数。 核对现金流正负号、NAV、基准时间与多解；不是基金真实业绩数据。
5. [`apache/fineract`](https://github.com/apache/fineract)：贷款、账户和金融服务平台的公开实现参考。 小微金融平台不等于大型银行对公核心；生产、监管和安全适配未评估。
6. [`apache/fineract-cn-accounting`](https://github.com/apache/fineract-cn-accounting)：历史 Fineract CN 账务模块；不是当前 Fineract 主线 · 仅作阅读参考
7. [`apache/fineract-cn-portfolio`](https://github.com/apache/fineract-cn-portfolio)：历史 Fineract CN 贷款模块；不是当前 Fineract 主线 · 仅作阅读参考
8. [`apache/incubator-kie`](https://github.com/apache/incubator-kie)：KIE/Drools 通用规则引擎，供合成授信规则示例使用
9. [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework)：企业应收应付、会计到银行对账的 ERP 侧接口
10. [`Arelle/Arelle`](https://github.com/Arelle/Arelle)：XBRL/iXBRL 解析与校验，注意单位、期间和修订 · 仅作阅读参考
11. [`attack68/rateslib`](https://github.com/attack68/rateslib)：利率和 FX 曲线许可先行阅读参考；不是开源复用建议 · 仅作阅读参考
12. [`bbcho/risktools-dev`](https://github.com/bbcho/risktools-dev)：商品期货到期约定、平均价掉期和能源数据适配；商业数据权限另查
13. [`beancount/beancount`](https://github.com/beancount/beancount)：用合成仓位、现金与股息核对分录；非中央存管系统
14. [`beancount/fava`](https://github.com/beancount/fava)：浏览复式记账资金流、账户和多币种报告
15. [`besu-eth/besu`](https://github.com/besu-eth/besu)：代币化实验的以太坊基础设施；不是证券资产服务
16. [`bradbase/xlcalculator`](https://github.com/bradbase/xlcalculator)：Excel 公式分析；明确支持函数与公式缺失 · 仅作阅读参考
17. [`CMTA/CMTAT`](https://github.com/CMTA/CMTAT)：研究证券型代币发行与事件处理，独立于传统承销
18. [`coinbase/coinbase-sdk-nodejs`](https://github.com/coinbase/coinbase-sdk-nodejs)：数字资产开发接口样例；客户资产和密钥仍受独立控制 · 仅作阅读参考
19. [`csingley/ofxtools`](https://github.com/csingley/ofxtools)：OFX 投资交易、持仓与账户报表解析；非 Swift 交收指令 · 仅作阅读参考
20. [`daconjurer/ctmds`](https://github.com/daconjurer/ctmds)：合成电力、原油和天然气价格的生成参考；不是实际市场记录 · 仅作阅读参考
21. [`databricks-industry-solutions/lakehouse-industry-data-models`](https://github.com/databricks-industry-solutions/lakehouse-industry-data-models)：银行模型中的信用证、提款和交易表；不是运行中的银行账簿 · 仅作阅读参考
22. [`datalab-to/marker`](https://github.com/datalab-to/marker)：PDF 到结构化文本；代码与模型各按其条款
23. [`Deed3Labs/Protocol-Contracts`](https://github.com/Deed3Labs/Protocol-Contracts)：证券型代币与链上信用研究原型；非法律确权或受监管资产托管
24. [`deutschebank/dbMango`](https://github.com/deutschebank/dbMango)：带角色控制、审计和数据操作功能的 MongoDB 管理工具。 README 明确一个德银专有数据插件不公开；不是信贷/支付引擎，不采集该插件。 · 仅作阅读参考
25. [`deutschebank/deutsche-bank-api-program`](https://github.com/deutschebank/deutsche-bank-api-program)：开放银行 API、沙盒和开发示例。 不等于已开放完整对公 API，也不是 Autobahn 定价引擎。 · 仅作阅读参考
26. [`dgunning/edgartools`](https://github.com/dgunning/edgartools)：借款人财务期次及重述研究
27. [`digital-asset/canton`](https://github.com/digital-asset/canton)：同步器与权限式账本；非监管托管产品
28. [`digital-asset/daml`](https://github.com/digital-asset/daml)：合约权限、观察者与账本 API；非托管业务实现
29. [`digital-asset/daml-finance`](https://github.com/digital-asset/daml-finance)：抵押品及交易生命周期
30. [`ebics-java/ebics-java-client`](https://github.com/ebics-java/ebics-java-client)：基于 Java 的 EBICS 银行文件交换
31. [`eddelbuettel/rquantlib`](https://github.com/eddelbuettel/rquantlib)：QuantLib 的 R 接口，含债券、期限结构及期权参考 · 仅作阅读参考
32. [`eliot-tabet/pfc_constructor`](https://github.com/eliot-tabet/pfc_constructor)：商品远期、期货和掉期曲线插值；需核对交割期与体积权重 · 仅作阅读参考
33. [`energyquantified/eq-python-client`](https://github.com/energyquantified/eq-python-client)：电力、燃料与排放曲线的数据接口；订阅权限与代码许可分开
34. [`equinor/curvy`](https://github.com/equinor/curvy)：从分期电力远期合约构建连续电价曲线；实验复现需自备有权数据
35. [`ethereum/ERCs`](https://github.com/ethereum/ERCs)：数字资产标准示例；各文件条款与业务用途分别核对
36. [`FinancePy-Org/FinancePy`](https://github.com/FinancePy-Org/FinancePy)：合成企业外汇对冲研究
37. [`finmath/finmath-lib`](https://github.com/finmath/finmath-lib)：Java 利率模型、蒙特卡洛与衍生品对照
38. [`finos/common-domain-model`](https://github.com/finos/common-domain-model)：公司套保事件与账务映射 · 仅作阅读参考
39. [`finos/FDC3`](https://github.com/finos/FDC3)：金融桌面上下文、intent 与应用互操作标准。 规范、软件及相关商标/实现权利分开；不是任何银行专有终端代码。 · 仅作阅读参考
40. [`finos/legend`](https://github.com/finos/legend)：Legend 总入口：数据建模、映射、治理。 当前为 FINOS 项目，不等于 GS 内部模型和客户数据。
41. [`finos/legend-engine`](https://github.com/finos/legend-engine)：Legend 执行与服务层，与 Studio 界面分开阅读。 数据源连接的权限与各数据库条款必须单独获得。
42. [`finos/legend-pure`](https://github.com/finos/legend-pure)：对公数据与规则模型的金融 DSL
43. [`finos/legend-studio`](https://github.com/finos/legend-studio)：数据建模和服务工作流前端。 本轮不安装，不宣称已形成银行级数据治理部署。
44. [`finos/morphir`](https://github.com/finos/morphir)：业务逻辑的类型化建模和可移植中间表示。 信贷决策/定价是拟议研究方向，不是本轮验证结果。
45. [`finos/plexus-interop`](https://github.com/finos/plexus-interop)：历史 Autobahn 桌面互操作架构。 归档项目只作历史参考；没有开放 Autobahn 的完整业务代码。 · 仅作阅读参考
46. [`finos/waltz`](https://github.com/finos/waltz)：应用、数据流和企业架构依赖地图。 是企业架构工具，不是直接产生贷款定价或交易信号。
47. [`fireblocks/ts-sdk`](https://github.com/fireblocks/ts-sdk)：数字资产服务的客户端；不是密钥托管实现
48. [`firefly-iii/firefly-iii`](https://github.com/firefly-iii/firefly-iii)：用虚拟账本研究净资产、预算与定期账单，不导入真实账户
49. [`formancehq/ledger`](https://github.com/formancehq/ledger)：可编程复式总账与余额核对
50. [`frappe/erpnext`](https://github.com/frappe/erpnext)：企业总账、出纳和现金对账；不是银行核心 · 仅作阅读参考
51. [`frictionlessdata/frictionless-py`](https://github.com/frictionlessdata/frictionless-py)：验证可比公司与先例交易数据的 schema
52. [`ghostfolio/ghostfolio`](https://github.com/ghostfolio/ghostfolio)：多账户持仓、资产配置和个人收益追踪，不是银行财富管理系统
53. [`Gnucash/gnucash`](https://github.com/Gnucash/gnucash)：多币种账簿及证券事件的对账参照 · 仅作阅读参考
54. [`goldmansachs/docknight_lib`](https://github.com/goldmansachs/docknight_lib)：文档结构和表格抽取，研究财务文档输入层。 抽取结果需要页码溯源和人工核对；不是完整尽调引擎。
55. [`goldmansachs/gs-quant`](https://github.com/goldmansachs/gs-quant)：发行估值和市场研究 SDK
56. [`goldmansachs/jdmn`](https://github.com/goldmansachs/jdmn)：DMN 决策表和规则执行，可研究审批规则的显式建模。 信贷准入规则只是拟议用途；不代表 GS 的授信模型。
57. [`goldmansachs/obevo`](https://github.com/goldmansachs/obevo)：大型数据库 schema 变更、可审计部署和环境管理。 工具不包含银行真实 schema、风控政策或生产访问权限。
58. [`goldmansachs/reladomo`](https://github.com/goldmansachs/reladomo)：Java 对象关系映射、事务和双时态数据建模参考。 通用工程基础设施，不是银行账务系统或客户数据。
59. [`google/tf-quant-finance`](https://github.com/google/tf-quant-finance)：债券、利率及期权数值方法；运行性能未测试
60. [`herrrickshaw/financial-analysis-toolkit-public`](https://github.com/herrrickshaw/financial-analysis-toolkit-public)：个人 DCF、可比、并购与 LBO 工具；模型未独立重算 · 仅作阅读参考
61. [`hyperledger-cacti/cacti`](https://github.com/hyperledger-cacti/cacti)：异构账本互操作；不等同证券 CSD
62. [`hyperledger-labs/harmonia`](https://github.com/hyperledger-labs/harmonia)：模拟 PvP/DvP 失败路径 · 仅作阅读参考
63. [`hyperledger-labs/weaver-dlt-interoperability`](https://github.com/hyperledger-labs/weaver-dlt-interoperability)：历史跨账本状态证明与交收参考 · 仅作阅读参考
64. [`HyperledgerHandsOn/trade-finance-logistics`](https://github.com/HyperledgerHandsOn/trade-finance-logistics)：信用证与装运交接的历史教学原型 · 仅作阅读参考
65. [`ib-api-reloaded/ib_async`](https://github.com/ib-api-reloaded/ib_async)：券商接口可用于阅读仓位和事件；非托管实现，不连接账户
66. [`ildrm/madar-investment-operations-platform`](https://github.com/ildrm/madar-investment-operations-platform)：基金会计、NAV 和对账的项目；未做生产或监管验收
67. [`janestreet/incremental`](https://github.com/janestreet/incremental)：研究曲线依赖的增量更新；非交易算法
68. [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit)：公司信贷财务比率与债务指标
69. [`joseprupi/quantraserver`](https://github.com/joseprupi/quantraserver)：基于 QuantLib 的无状态定价服务；接口约定、数值精度与服务条款另核
70. [`jpmorganchase/abides-jpmc-public`](https://github.com/jpmorganchase/abides-jpmc-public)：代理驱动的市场模拟与微观结构研究。 模拟输出不是可交易 alpha，也不是并购估值。 · 仅作阅读参考
71. [`jpmorganchase/dataquery-sdk`](https://github.com/jpmorganchase/dataquery-sdk)：DataQuery 的查询、下载、重试和配额处理。 DataQuery 与 Fusion 不是同一服务；必须单独核对数据订阅和认证。
72. [`jpmorganchase/fusion`](https://github.com/jpmorganchase/fusion)：Fusion 数据平台 Python SDK；区分发现、下载和数据权限。 需按产品注册、认证及订阅权益使用；SDK 不提供免费数据。 · 仅作阅读参考
73. [`jpmorganchase/fusion-java-sdk`](https://github.com/jpmorganchase/fusion-java-sdk)：Fusion 的 Java 数据接入接口。 同样受账户、产品条款和数据授权约束。 · 仅作阅读参考
74. [`jpmorganchase/fusion-notebooks`](https://github.com/jpmorganchase/fusion-notebooks)：阅读 PyFusion 的工作流示例和 notebook。 示例不是已验证的投资研究结果；不要提交账户配置。 · 仅作阅读参考
75. [`jpmorganchase/PADL`](https://github.com/jpmorganchase/PADL)：隐私、可审计分布式账本与零知识证明研究。 不是 Kinexys 的完整生产支付系统，未在本轮运行。
76. [`jpmorganchase/python-training`](https://github.com/jpmorganchase/python-training)：面向分析师/交易者的 Python 学习材料。 培训仓库不是 JPM 生产模型、投行岗位认证或策略。
77. [`jpmorganchase/SFinX`](https://github.com/jpmorganchase/SFinX)：数值、指标、期间型 Excel 表格的标准化抽取，输出 TSV/JSON。 已归档；不是通用 LLM 财报抽取器，也不可替代财报审计或事实核验。 · 仅作阅读参考
78. [`lballabio/QuantLib`](https://github.com/lballabio/QuantLib)：日期与贷款现金流研究 · 仅作阅读参考
79. [`lballabio/QuantLib-SWIG`](https://github.com/lballabio/QuantLib-SWIG)：QuantLib 的 Python 等语言绑定，不是第二个独立模型 · 仅作阅读参考
80. [`ledger/ledger`](https://github.com/ledger/ledger)：用于合成券、款和分录核对的通用复式账簿 · 仅作阅读参考
81. [`libfintx/libfintx`](https://github.com/libfintx/libfintx)：FinTS 等渠道接入，支持范围以固定版本为准
82. [`LMAX-Exchange/disruptor`](https://github.com/LMAX-Exchange/disruptor)：报价事件排序的通用并发组件；不是 FX 撮合器
83. [`man-group/arctic`](https://github.com/man-group/arctic)：历史市场时间序列架构；与 ArcticDB 区分
84. [`man-group/ArcticDB`](https://github.com/man-group/ArcticDB)：版本化时间序列；目前许可按具体 tag 核对 · 仅作阅读参考
85. [`microsoft/markitdown`](https://github.com/microsoft/markitdown)：文档转文本与模型输入溯源；需人工核对页码
86. [`mojaloop/mojaloop`](https://github.com/mojaloop/mojaloop)：支付系统互操作架构；不是企业资金池 · 仅作阅读参考
87. [`moov-io/ach`](https://github.com/moov-io/ach)：美国 ACH 文件的读取、生成与校验。 格式库不提供清算会员资格、银行连接或付款授权。
88. [`moov-io/fedwire20022`](https://github.com/moov-io/fedwire20022)：Fedwire Funds ISO 20022 报文
89. [`moov-io/iso8583`](https://github.com/moov-io/iso8583)：银行卡消息解析；与 ACH 及 ISO 20022 区分
90. [`moov-io/wire`](https://github.com/moov-io/wire)：历史 Fedwire FAIM 消息的读取、校验与迁移参考。 已归档；README 说明 FAIM 不再用于实时 Fedwire，不能作为新接入推荐。wire20022 也已弃用，当前入口为 fedwire20022。 · 仅作阅读参考
91. [`moov-io/wire20022`](https://github.com/moov-io/wire20022)：旧 Fedwire ISO 20022 代码；仅作迁移追踪 · 仅作阅读参考
92. [`morganstanley/api`](https://github.com/morganstanley/api)：MS API Program 的样例和开发入口。 样例不授予产品、账户、支付或客户资料权限。
93. [`morganstanley/ComposeUI`](https://github.com/morganstanley/ComposeUI)：混合桌面容器与应用集成，可用于研究终端原型。 UI 容器不是可交易、已认证的投行终端。
94. [`morganstanley/desktopJS`](https://github.com/morganstanley/desktopJS)：跨 HTML5 桌面容器的接口抽象。 只收录架构参考；维护状态以快照为准。
95. [`morganstanley/optimus-cirrus`](https://github.com/morganstanley/optimus-cirrus)：Optimus 工程体系；研究依赖计算、缓存和数据处理边界。 README 仍提示构建工具引导工作；未验证可独立构建，不可声称获得 MS 估值/风险模型。
96. [`morganstanley/pyfixmsg`](https://github.com/morganstanley/pyfixmsg)：FIX 消息解析、修改、序列化与测试。 FIX 解析器不包含交易所接入、会话管理或下单授权。 · 仅作阅读参考
97. [`morganstanley/testplan`](https://github.com/morganstanley/testplan)：多层级测试、系统集成验收与报告。 属于通用测试基础设施，金融正确性仍需独立 oracle。
98. [`mortada/fredapi`](https://github.com/mortada/fredapi)：FRED/ALFRED 公共数据客户端；历史分析应标明 vintage
99. [`Nachidoestech/lbo-model`](https://github.com/Nachidoestech/lbo-model)：杠杆收购、债务偿还、退出倍数和 IRR/MOIC 的教学模型。 非 PE 机构官方模型；财务闭环、费用和情景鲁棒性尚未运行验证。
100. [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader)：多资产事件驱动研究；具体期货与 FX 支持按连接器核对
101. [`Nityahapani/finverse`](https://github.com/Nityahapani/finverse)：个人研究：财报、DCF、LBO；ML 假设未经独立验证
102. [`numpy/numpy-financial`](https://github.com/numpy/numpy-financial)：周期现金流 NPV、IRR、年金和资金时间价值。 周期 IRR 不替代不规则日期 XIRR；多根与不存在解需要负对照。
103. [`oldhero5/energex`](https://github.com/oldhero5/energex)：电力数据的双时间版本及回放；源可见，商业使用受限 · 仅作阅读参考
104. [`Open-Cap-Table-Coalition/Open-Cap-Format-OCF`](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF)：融资轮与稀释的结构化输入 · 仅作阅读参考
105. [`OpenBankProject/OBP-API`](https://github.com/OpenBankProject/OBP-API)：开放银行 API 框架与沙盒，不提供真实账户权限
106. [`openbq-org/OpenBB`](https://github.com/openbq-org/OpenBB)：报告、市场数据与研究入口；数据订阅独立 · 仅作阅读参考
107. [`OpenFIGI/api-examples`](https://github.com/OpenFIGI/api-examples)：FIGI 标识映射示例；不是证券持仓记录
108. [`openMF/mifosx-platform`](https://github.com/openMF/mifosx-platform)：小额金融核心功能与 Fineract 集成边界；不是运行任何银行内部系统
109. [`openMF/web-app`](https://github.com/openMF/web-app)：Mifos/Fineract 账户、贷款运营界面
110. [`OpenSourceRisk/Engine`](https://github.com/OpenSourceRisk/Engine)：曲线配置、估值、敏感度、情景和组合风险 · 仅作阅读参考
111. [`OpenZeppelin/openzeppelin-contracts`](https://github.com/OpenZeppelin/openzeppelin-contracts)：数字资产通用合约组件；不代表实际托管承诺
112. [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective)：表格、流式数据、透视分析与可视化。 使用当前规范仓库，旧 finos/perspective 会重定向；不代表 JPM 投资引擎。
113. [`Point72/csp`](https://github.com/Point72/csp)：回放曲线事件与检查时间戳；不是策略源码
114. [`Point72/csp-gateway`](https://github.com/Point72/csp-gateway)：事件网关与服务组合；不拥有市场接入资格
115. [`Point72/raydar`](https://github.com/Point72/raydar)：数据时间线和面板工程参考；不是报价源或交易系统
116. [`portfolio-performance/portfolio`](https://github.com/portfolio-performance/portfolio)：组合仓位与派息记录参考，不提供托管账户授权
117. [`prowide/prowide-core`](https://github.com/prowide/prowide-core)：银行 SWIFT MT 消息编码
118. [`prowide/prowide-iso20022`](https://github.com/prowide/prowide-iso20022)：pain 支付发起、camt 现金报告、pacs 清算
119. [`pydata/pandas-datareader`](https://github.com/pydata/pandas-datareader)：宏观数据连接器；观察期不等于发布日期 · 仅作阅读参考
120. [`PyPortfolio/PyPortfolioOpt`](https://github.com/PyPortfolio/PyPortfolioOpt)：研究虚拟产品组合的配置逻辑，不是适当性建议
121. [`PyPSA/PyPSA`](https://github.com/PyPSA/PyPSA)：电力现货物理系统及节点边际成本；非衍生品或实时报价源
122. [`QuantConnect/Lean`](https://github.com/QuantConnect/Lean)：外汇、期货研究与事件模拟；数据服务和成交规则另核
123. [`quants-net/PyFENG`](https://github.com/quants-net/PyFENG)：期权模型与波动率数值对照
124. [`quickfix-j/quickfixj`](https://github.com/quickfix-j/quickfixj)：Java FIX 会话与消息；交易账户和交易所准入另行取得 · 仅作阅读参考
125. [`quickfix/quickfix`](https://github.com/quickfix/quickfix)：资本市场 FIX 工程 · 仅作阅读参考
126. [`raphaelm/python-sepaxml`](https://github.com/raphaelm/python-sepaxml)：SEPA pain.001 批量付款和 pain.008 扣款文件
127. [`safe-fndn/safe-smart-account`](https://github.com/safe-fndn/safe-smart-account)：多签合约和链上权限控制示例；不等同传统托管
128. [`schulluk/ebicsclient`](https://github.com/schulluk/ebicsclient)：EBICS 银企直联文件、密钥初始化与传输
129. [`sebastienrousseau/bankstatementparser`](https://github.com/sebastienrousseau/bankstatementparser)：CAMT、MT940、BAI2 银行报表归一化 · 仅作阅读参考
130. [`sec-edgar/sec-edgar`](https://github.com/sec-edgar/sec-edgar)：SEC 申报文件批量读取；遵守官方访问政策
131. [`SixSigmaEngineer/valuation-models`](https://github.com/SixSigmaEngineer/valuation-models)：教育参考：DCF、LBO、协同价值和表格
132. [`tradingtechnologies/Strata`](https://github.com/tradingtechnologies/Strata)：债券发行估值和敏感度
133. [`vinci1it2000/formulas`](https://github.com/vinci1it2000/formulas)：把 Excel 公式解析为 Python 计算图；非 Excel 完整替代
134. [`wealthfolio/wealthfolio`](https://github.com/wealthfolio/wealthfolio)：本地持仓分组和收益口径；可选券商同步属于单独服务，不连接账户
135. [`wechatpay-apiv3/wechatpay-apache-httpclient`](https://github.com/wechatpay-apiv3/wechatpay-apache-httpclient)：Java API 的 HTTP 层与请求签名
136. [`wechatpay-apiv3/wechatpay-global-skills`](https://github.com/wechatpay-apiv3/wechatpay-global-skills)：跨境收款、回调与商户结算
137. [`wechatpay-apiv3/wechatpay-go`](https://github.com/wechatpay-apiv3/wechatpay-go)：商户支付接入与签名
138. [`wechatpay-apiv3/wechatpay-java`](https://github.com/wechatpay-apiv3/wechatpay-java)：Java 支付请求、签名和回调
139. [`wechatpay-apiv3/wechatpay-php`](https://github.com/wechatpay-apiv3/wechatpay-php)：PHP 支付请求、签名与回调
140. [`wechatpay-apiv3/wechatpay-skills`](https://github.com/wechatpay-apiv3/wechatpay-skills)：境内支付接入与离线证书诊断
141. [`wolph/mt940`](https://github.com/wolph/mt940)：SWIFT MT940 银行报表解析与对账
142. [`XTXMarkets/ternfs`](https://github.com/XTXMarkets/ternfs)：研究数据文件存储；不含曲线、订单或报价 · 仅作阅读参考
143. [`yellowbean/AbsBox`](https://github.com/yellowbean/AbsBox)：结构化发行分层与分派
144. [`zerodrift/leanetrm`](https://github.com/zerodrift/leanetrm)：能源和商品曲线、风险、交易生命周期的 ETRM 原型；非生产验证

</details>

<details>
<summary>PE / 私募股权（16）</summary>

[Private Equity / 私募股权](private-equity/README.md)

1. [`alephdata/aleph`](https://github.com/alephdata/aleph)：研究调查文档检索与交叉引用；关联提示需人工核对 · 仅作阅读参考
2. [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr)：以合成不规则募集和退出现金流验证 XIRR
3. [`captableinc/captable`](https://github.com/captableinc/captable)：读股权台账、持有人和持股变化的产品工作流
4. [`captablex/captablex`](https://github.com/captablex/captablex)：对照股类、优先权和退出瀑布的工程模型，未验证任何基金条款
5. [`dgunning/edgartools`](https://github.com/dgunning/edgartools)：追踪尽调财报的申报期和修订
6. [`EQTPartners/CompanyKG`](https://github.com/EQTPartners/CompanyKG)：以公开说明研究企业图与相似度任务；单独核查语料再利用条款 · 仅作阅读参考
7. [`ildrm/madar-investment-operations-platform`](https://github.com/ildrm/madar-investment-operations-platform)：阅读投资运营与可追溯台账架构，不代表 GP 一体化系统
8. [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit)：复查财务比率与可比估值输入
9. [`Nachidoestech/lbo-model`](https://github.com/Nachidoestech/lbo-model)：拆解合成并购融资、债务偿还与退出杠杆
10. [`numpy/numpy-financial`](https://github.com/numpy/numpy-financial)：用合成等间隔现金流核对 NPV 与 IRR
11. [`Open-Cap-Table-Coalition/ocx`](https://github.com/Open-Cap-Table-Coalition/ocx)：查看资本结构事件在 OCF 与内部数据模型之间怎样转换
12. [`Open-Cap-Table-Coalition/Open-Cap-Format-OCF`](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF)：对比持股、证券类别和既有股权事件的交换格式 · 仅作阅读参考
13. [`openownership/data-standard`](https://github.com/openownership/data-standard)：用 BODS 的实体、权益人和持有关系建受益所有权核查字段 · 仅作阅读参考
14. [`openownership/lib-cove-bods`](https://github.com/openownership/lib-cove-bods)：校验 BODS 樣例版本、必填字段与非法关系 · 仅作阅读参考
15. [`opensanctions/yente`](https://github.com/opensanctions/yente)：用合成人名比较制裁筛查匹配和误报；法律判断与数据授权独立 · 仅作阅读参考
16. [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective)：用合成投后指标搭配切片和汇总

</details>

<details>
<summary>VC / 创业投资（12）</summary>

[Venture Capital / 创业投资](venture-capital/README.md)

1. [`alephdata/aleph`](https://github.com/alephdata/aleph)：用虚拟公司资料对照检索和实体关联，不把命中当尽调结论 · 仅作阅读参考
2. [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr)：对虚拟持股轮次与退出现金流做日期敏感性分析
3. [`captableinc/captable`](https://github.com/captableinc/captable)：以虚拟轮次研究初创股权台账，不写入真实股东
4. [`captablex/captablex`](https://github.com/captablex/captablex)：使用虚拟股东、股类和融资轮次对照 OCF 交换及退出瀑布；不保存真实名册
5. [`EQTPartners/CompanyKG`](https://github.com/EQTPartners/CompanyKG)：研究企业网络筛选的验证协议，不作为企业质量或融资信号 · 仅作阅读参考
6. [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit)：用虚拟报表核对现金流、增长和估值假设
7. [`joelparkerhenderson/pitch-deck`](https://github.com/joelparkerhenderson/pitch-deck)：用公开材料框架设计商业模式和融资叙事的审阅清单，不是投资工具 · 仅作阅读参考
8. [`numpy/numpy-financial`](https://github.com/numpy/numpy-financial)：比较投资情景下折现和期内回报；不把等间隔 IRR 当 XIRR
9. [`Open-Cap-Table-Coalition/ocx`](https://github.com/Open-Cap-Table-Coalition/ocx)：用合成股权事件练习 OCF 输入校验和交换
10. [`Open-Cap-Table-Coalition/Open-Cap-Format-OCF`](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF)：用虚拟股东与轮次验证 cap table 事件交换和稀释 · 仅作阅读参考
11. [`openownership/data-standard`](https://github.com/openownership/data-standard)：比较公开股权来源的时间、证明材料及冲突 · 仅作阅读参考
12. [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective)：比较不同虚拟融资轮次的经营指标，不存放标的私有数据

</details>

<details>
<summary>Securities / 券商与证券（14）</summary>

[Securities / 券商与证券](securities/README.md)

1. [`alpacahq/alpaca-py`](https://github.com/alpacahq/alpaca-py)：分辨市场数据、交易及模拟环境客户端；不调用实盘
2. [`connamara/quickfixn`](https://github.com/connamara/quickfixn)：对比 FIX 会话序列号、重发与拒绝路径的 .NET 实现 · 仅作阅读参考
3. [`finos/common-domain-model`](https://github.com/finos/common-domain-model)：按生命周期研究证券及衍生品事件，不是路由系统 · 仅作阅读参考
4. [`ib-api-reloaded/ib_async`](https://github.com/ib-api-reloaded/ib_async)：以只读或模拟流程读券商账户与订单状态机；不下单
5. [`jpmorganchase/abides-jpmc-public`](https://github.com/jpmorganchase/abides-jpmc-public)：用合成代理研究订单执行、延迟与成交轨迹 · 仅作阅读参考
6. [`kernc/backtesting.py`](https://github.com/kernc/backtesting.py)：用透明的例子核对交易信号到虚拟成交的规则
7. [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader)：核对订单生命周期处理与仿真/实盘界限
8. [`OpenFIGI/api-examples`](https://github.com/OpenFIGI/api-examples)：核对股票标识映射的歧义、市场及证券类别
9. [`QuantBox/XAPI3`](https://github.com/QuantBox/XAPI3)：对比国内市场交易接口抽象；驱动许可与实盘账户另核 · 仅作阅读参考
10. [`QuantConnect/Lean`](https://github.com/QuantConnect/Lean)：研究虚拟订单和券商模型抽象，禁用实盘
11. [`quickfix-j/quickfixj`](https://github.com/quickfix-j/quickfixj)：用 Java 工具研究订单状态及 FIX 会话 · 仅作阅读参考
12. [`quickfix/quickfix`](https://github.com/quickfix/quickfix)：证券订单消息的会话、回执与重连机制 · 仅作阅读参考
13. [`stefan-jansen/zipline-reloaded`](https://github.com/stefan-jansen/zipline-reloaded)：按交易日历复查模拟订单的时间和成交条件
14. [`vnpy/vnpy`](https://github.com/vnpy/vnpy)：读事件驱动交易系统、网关与模拟模式；实盘适配独立审查

</details>

<details>
<summary>Exchange / 交易所（15）</summary>

[Exchange / 交易所](exchanges/README.md)

1. [`binance/binance-connector-python`](https://github.com/binance/binance-connector-python)：数字资产场所 REST 和流式接口示例；账户、市场和地区条款另核 · 仅作阅读参考
2. [`ccxt/ccxt`](https://github.com/ccxt/ccxt)：比较不同数字资产交易场所的接口适配，不等同监管交易所或实盘认证 · 仅作阅读参考
3. [`coinbase/coinbase-advanced-py`](https://github.com/coinbase/coinbase-advanced-py)：数字资产交易场所的官方客户端；不是传统证券交易所实现 · 仅作阅读参考
4. [`connamara/quickfixn`](https://github.com/connamara/quickfixn)：用模拟参与者消息检验顺序与回执，不连接交易所 · 仅作阅读参考
5. [`databento/databento-python`](https://github.com/databento/databento-python)：读逐笔和订单簿数据的解码接口，不复制有权数据 · 仅作阅读参考
6. [`enewhuis/liquibook`](https://github.com/enewhuis/liquibook)：研究限价订单、部分成交和撤单的 C++ 撮合组件 · 仅作阅读参考
7. [`exchange-core/exchange-core`](https://github.com/exchange-core/exchange-core)：读订单簿、撮合和风险检查的模拟实现，不推断真实场所部署
8. [`finos/common-domain-model`](https://github.com/finos/common-domain-model)：阅读交易后生命周期及结算事件的规范表示 · 仅作阅读参考
9. [`J-Quants/jquants-api-client-python`](https://github.com/J-Quants/jquants-api-client-python)：读日本上市证券数据服务的分页和交易日语义，不是撮合引擎 · 仅作阅读参考
10. [`jpmorganchase/abides-jpmc-public`](https://github.com/jpmorganchase/abides-jpmc-public)：比较合成市场下撮合与参与者事件回放 · 仅作阅读参考
11. [`LMAX-Exchange/disruptor`](https://github.com/LMAX-Exchange/disruptor)：读取事件分发工程组件；不代表场所交易或撮合系统
12. [`Nasdaq/data-link-python`](https://github.com/Nasdaq/data-link-python)：交易所品牌数据服务客户端；非交易接入或交易所主系统 · 仅作阅读参考
13. [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader)：用虚拟场所适配器对照市场回放事件
14. [`quickfix-j/quickfixj`](https://github.com/quickfix-j/quickfixj)：检查测试场所客户端的心跳、断线和重发行为 · 仅作阅读参考
15. [`quickfix/quickfix`](https://github.com/quickfix/quickfix)：模拟参与者和场所之间的 FIX 消息与序列 · 仅作阅读参考

</details>

<details>
<summary>Fund / 基金与资产管理（20）</summary>

[Funds & Asset Management / 基金与资产管理](funds/README.md)

1. [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr)：区分资金加权收益和时间加权收益
2. [`cvxgrp/cvxportfolio`](https://github.com/cvxgrp/cvxportfolio)：研究考虑交易和持有成本的组合优化及回测
3. [`dcajasn/Riskfolio-Lib`](https://github.com/dcajasn/Riskfolio-Lib)：在虚拟收益序列上对照风险度量和资产权重约束
4. [`formancehq/ledger`](https://github.com/formancehq/ledger)：演练虚拟结算现金、费用和分账的复式过账
5. [`ildrm/madar-investment-operations-platform`](https://github.com/ildrm/madar-investment-operations-platform)：研究持仓和运营数据工作流，输入和数据模型需独立验证
6. [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit)：比较基本面和组合研究使用的财务字段口径
7. [`kernc/backtesting.py`](https://github.com/kernc/backtesting.py)：在冻结的合成价格上比较回测与基准净值
8. [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader)：研究基于事件的资产组合仿真、成本和执行假设
9. [`openbq-org/OpenBB`](https://github.com/openbq-org/OpenBB)：比较研究数据接口的字段一致性和覆盖边界 · 仅作阅读参考
10. [`pmorissette/bt`](https://github.com/pmorissette/bt)：用权重和交易规则构建可审查的策略模拟
11. [`pmorissette/ffn`](https://github.com/pmorissette/ffn)：比较从价格计算的比例收益和组合统计
12. [`polakowo/vectorbt`](https://github.com/polakowo/vectorbt)：向量化组合模拟读码；公共版与商业条款需分开 · 仅作阅读参考
13. [`portfolio-performance/portfolio`](https://github.com/portfolio-performance/portfolio)：用合成净值对照时间加权收益与报告口径
14. [`PyPortfolio/PyPortfolioOpt`](https://github.com/PyPortfolio/PyPortfolioOpt)：用固定协方差与预期收益比较权重、目标和约束
15. [`QuantConnect/Lean`](https://github.com/QuantConnect/Lean)：用固定模拟价格测试组合、费用和执行假设
16. [`ranaroussi/quantstats`](https://github.com/ranaroussi/quantstats)：从日收益序列生成报告，比较基准、回撤和风险口径
17. [`skfolio/skfolio`](https://github.com/skfolio/skfolio)：研究组合风险和交叉验证；不能把验证泄漏当超额收益
18. [`stefan-jansen/empyrical-reloaded`](https://github.com/stefan-jansen/empyrical-reloaded)：用于离线校对收益、回撤及风险统计的定义
19. [`stefan-jansen/pyfolio-reloaded`](https://github.com/stefan-jansen/pyfolio-reloaded)：把组合收益、头寸与成交汇总为研究用绩效报告
20. [`stefan-jansen/zipline-reloaded`](https://github.com/stefan-jansen/zipline-reloaded)：逐期策略回测与交易成本模型，注意点时数据和退市偏差

</details>

<details>
<summary>Insurance / 保险（9）</summary>

[Insurance / 保险](insurance/README.md)

1. [`casact/chainladder-python`](https://github.com/casact/chainladder-python)：检查赔付三角、发展因子和准备金估计的输入假设
2. [`CLIMADA-project/climada_python`](https://github.com/CLIMADA-project/climada_python)：研究灾害、暴露、脆弱性和适应策略的模型组合
3. [`lifelib-dev/lifelib`](https://github.com/lifelib-dev/lifelib)：用公开合成情景读寿险现金流、利润测试和模型结构
4. [`mages/ChainLadder`](https://github.com/mages/ChainLadder)：以 R 复查赔付三角与准备金方法，与 Python 原理对照 · 仅作阅读参考
5. [`OasisLMF/OasisLMF`](https://github.com/OasisLMF/OasisLMF)：读暴露、灾害和赔付模拟框架；商业模型和风险数据另授权
6. [`OasisLMF/OasisPiWind`](https://github.com/OasisLMF/OasisPiWind)：用示例风险模型学习 Oasis 输入与损失流程，不用于真实承保
7. [`openimis/openimis-be-claim_py`](https://github.com/openimis/openimis-be-claim_py)：读医疗索赔状态和复核模块；仅用虚拟病历 · 仅作阅读参考
8. [`openimis/openimis-be-policy_py`](https://github.com/openimis/openimis-be-policy_py)：读医疗保险保单状态和缴费关联；不上传被保人数据 · 仅作阅读参考
9. [`openimis/openimis-be_py`](https://github.com/openimis/openimis-be_py)：了解公共卫生保险后台模块、权限和业务扩展，不当商业保险核心 · 仅作阅读参考

</details>

<details>
<summary>Financial Data / 金融数据与企业信息（22）</summary>

[Financial Data / 金融数据与企业信息](financial-data/README.md)

1. [`akfamily/akshare`](https://github.com/akfamily/akshare)：独立中国及跨市场数据接口；每个来源的访问和转发条款单查 · 仅作阅读参考
2. [`Arelle/Arelle`](https://github.com/Arelle/Arelle)：核对 XBRL 标签、币种、期间和对齐验证 · 仅作阅读参考
3. [`databento/databento-python`](https://github.com/databento/databento-python)：授权行情 SDK；客户端许可不代表行情可转发 · 仅作阅读参考
4. [`dgunning/edgartools`](https://github.com/dgunning/edgartools)：读取 EDGAR 文档和财报解析入口，遵守 SEC 访问政策
5. [`J-Quants/jquants-api-client-python`](https://github.com/J-Quants/jquants-api-client-python)：日本市场授权数据客户端，单独核对套餐和使用权 · 仅作阅读参考
6. [`jpmorganchase/dataquery-sdk`](https://github.com/jpmorganchase/dataquery-sdk)：公开客户端与授权数据集分列，不调用服务
7. [`jpmorganchase/fusion`](https://github.com/jpmorganchase/fusion)：公开 SDK 的授权数据发现及访问边界 · 仅作阅读参考
8. [`LSEG-API-Samples/Example.DataLibrary.Python`](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python)：LSEG 数据库示例；要求服务授权，示例许可不含新闻与行情 · 仅作阅读参考
9. [`man-group/ArcticDB`](https://github.com/man-group/ArcticDB)：用自有时序数据研究版本化存储，不提供金融行情 · 仅作阅读参考
10. [`matthewgilbert/blp`](https://github.com/matthewgilbert/blp)：独立 Bloomberg API 封装；适用 Bloomberg SDK 与数据条款 · 仅作阅读参考
11. [`mortada/fredapi`](https://github.com/mortada/fredapi)：宏观序列、修订日期和访问约束；底层序列权利另查
12. [`Nasdaq/data-link-python`](https://github.com/Nasdaq/data-link-python)：核对数据集凭证、日期、分页与订阅口径 · 仅作阅读参考
13. [`openbq-org/OpenBB`](https://github.com/openbq-org/OpenBB)：读取多供应商的适配层；数据和商业组件权利另查 · 仅作阅读参考
14. [`OpenFIGI/api-examples`](https://github.com/OpenFIGI/api-examples)：证券标识映射示例，查询服务与示例许可分开
15. [`openownership/data-standard`](https://github.com/openownership/data-standard)：受益所有权交换格式，不含通用企业主数据授权 · 仅作阅读参考
16. [`openownership/lib-cove-bods`](https://github.com/openownership/lib-cove-bods)：受益所有权声明的结构验证辅助库 · 仅作阅读参考
17. [`opensanctions/yente`](https://github.com/opensanctions/yente)：围绕实体查询、别名与匹配 API 做合规工程读码 · 仅作阅读参考
18. [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective)：用自有表格研究交互聚合和数据展示，不是行情供应商
19. [`ranaroussi/yfinance`](https://github.com/ranaroussi/yfinance)：独立行情研究接口；核对 Yahoo 条款，不推断可商用或可分发 · 仅作阅读参考
20. [`sec-edgar/sec-edgar`](https://github.com/sec-edgar/sec-edgar)：研究公开申报检索及原文索引；需遵守访问频率
21. [`underloam/xbbg`](https://github.com/underloam/xbbg)：独立 Bloomberg 封装；仍需合法终端或数据服务权限 · 仅作阅读参考
22. [`waditu/tushare`](https://github.com/waditu/tushare)：中国证券数据接口；账号、积分和数据使用权不随源代码获得 · 仅作阅读参考

</details>

这里只收录已核验的公开资料，不等于全网清单、开源合规结论或应用能力验证。未运行上游代码、未拉取商业数据、未连接实盘：**NOT_RUN / UNMEASURED**。
