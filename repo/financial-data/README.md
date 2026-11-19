# Financial Data / 金融数据与企业信息

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 22 个公开仓库。

分开代码许可、服务订阅、数据转发和隐私义务。Bloomberg、Wind、企查查官方入口是服务参考，不计作仓库。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 先读[官方服务与数据边界](../../update/2026-11-20-finance-market-map.md#商业数据服务)：用虚拟数据验证字段和时间戳，不获取商业数据或私有凭证。

## 监管财报与解析

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`Arelle/Arelle`](https://github.com/Arelle/Arelle) | 核对 XBRL 标签、币种、期间和对齐验证 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/Arelle/Arelle/blob/b7594fb8dc7c6cbf4e283a7166ef879ddf0c253c/README.md) · [许可文件](https://github.com/Arelle/Arelle/blob/b7594fb8dc7c6cbf4e283a7166ef879ddf0c253c/LICENSE.md) | [IB](../investment-banking/README.md) |
| [`dgunning/edgartools`](https://github.com/dgunning/edgartools) | 读取 EDGAR 文档和财报解析入口，遵守 SEC 访问政策 | 未标记归档；`MIT` | [README](https://github.com/dgunning/edgartools/blob/e2cc982e0084fa8e46da78f09493d1767845c8b5/README.md) · [许可文件](https://github.com/dgunning/edgartools/blob/e2cc982e0084fa8e46da78f09493d1767845c8b5/LICENSE.txt) | [PE](../private-equity/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`sec-edgar/sec-edgar`](https://github.com/sec-edgar/sec-edgar) | 研究公开申报检索及原文索引；需遵守访问频率 | 未标记归档；`Apache-2.0` | [README](https://github.com/sec-edgar/sec-edgar/blob/97db601615ebedd49637fb4ed847b3f714114720/README.rst) · [许可文件](https://github.com/sec-edgar/sec-edgar/blob/97db601615ebedd49637fb4ed847b3f714114720/LICENSE) | [IB](../investment-banking/README.md) |

## 企业、受益所有权和证券标识

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`OpenFIGI/api-examples`](https://github.com/OpenFIGI/api-examples) | 证券标识映射示例，查询服务与示例许可分开 | 未标记归档；`Apache-2.0` | [README](https://github.com/OpenFIGI/api-examples/blob/56a0f365185f6ef42d0190407470f76d216b8a55/README.md) · [许可文件](https://github.com/OpenFIGI/api-examples/blob/56a0f365185f6ef42d0190407470f76d216b8a55/LICENSE) | [SEC](../securities/README.md) · [AC](../asset-custody/README.md) |
| [`openownership/data-standard`](https://github.com/openownership/data-standard) | 受益所有权交换格式，不含通用企业主数据授权 | 未标记归档；`NOASSERTION`；仅作阅读参考；标准文本、实现和数据分别核对 | [README](https://github.com/openownership/data-standard/blob/e8cc3fd7a7fe45c7ad3b542dc07a99847a7960aa/README.md) · [许可文件](https://github.com/openownership/data-standard/blob/e8cc3fd7a7fe45c7ad3b542dc07a99847a7960aa/LICENSE) | [PE](../private-equity/README.md) · [VC](../venture-capital/README.md) |
| [`openownership/lib-cove-bods`](https://github.com/openownership/lib-cove-bods) | 受益所有权声明的结构验证辅助库 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/openownership/lib-cove-bods/blob/481a6c2f263722047598ed7ba0870830bd249455/README.md) · [许可文件](https://github.com/openownership/lib-cove-bods/blob/481a6c2f263722047598ed7ba0870830bd249455/LICENSE) | [PE](../private-equity/README.md) |
| [`opensanctions/yente`](https://github.com/opensanctions/yente) | 围绕实体查询、别名与匹配 API 做合规工程读码 | 未标记归档；`MIT`；仅作阅读参考；服务代码与筛查数据集授权独立 | [README](https://github.com/opensanctions/yente/blob/7074db814a382971370c5840509c0c9ec69380e1/README.md) · [许可文件](https://github.com/opensanctions/yente/blob/7074db814a382971370c5840509c0c9ec69380e1/LICENSE) | [PE](../private-equity/README.md) |

## 行情、宏观与历史数据适配

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`databento/databento-python`](https://github.com/databento/databento-python) | 授权行情 SDK；客户端许可不代表行情可转发 | 未标记归档；`Apache-2.0`；仅作阅读参考；授权市场数据另需协议，不调用服务 | [README](https://github.com/databento/databento-python/blob/f6529f1062e0642fe52334d767a72f2a75244398/README.md) · [许可文件](https://github.com/databento/databento-python/blob/f6529f1062e0642fe52334d767a72f2a75244398/LICENSE) | [EX](../exchanges/README.md) |
| [`J-Quants/jquants-api-client-python`](https://github.com/J-Quants/jquants-api-client-python) | 日本市场授权数据客户端，单独核对套餐和使用权 | 未标记归档；`Apache-2.0`；仅作阅读参考；J-Quants 服务条款和订阅权限另核 | [README](https://github.com/J-Quants/jquants-api-client-python/blob/4a6ab360dbd43e763595f7ad362e749a25d6439d/README.md) · [许可文件](https://github.com/J-Quants/jquants-api-client-python/blob/4a6ab360dbd43e763595f7ad362e749a25d6439d/LICENSE) | [EX](../exchanges/README.md) |
| [`man-group/ArcticDB`](https://github.com/man-group/ArcticDB) | 用自有时序数据研究版本化存储，不提供金融行情 | 未标记归档；`NOASSERTION`；仅作阅读参考；许可及转换日期按具体版本核对 | [README](https://github.com/man-group/ArcticDB/blob/8de98c586982fd30f1d00f07b0b0422408231c4b/README.md) · [许可文件](https://github.com/man-group/ArcticDB/blob/8de98c586982fd30f1d00f07b0b0422408231c4b/LICENSE.txt) | [FICC](../ficc/catalog.md) |
| [`mortada/fredapi`](https://github.com/mortada/fredapi) | 宏观序列、修订日期和访问约束；底层序列权利另查 | 未标记归档；`Apache-2.0` | [README](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/README.md) · [许可文件](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/LICENSE) | [FICC](../ficc/catalog.md) |
| [`Nasdaq/data-link-python`](https://github.com/Nasdaq/data-link-python) | 核对数据集凭证、日期、分页与订阅口径 | 未标记归档；`MIT`；仅作阅读参考；数据集许可、套餐及再分发限制独立 | [README](https://github.com/Nasdaq/data-link-python/blob/431094f87292c3c566ddbd647296f65957ac2254/README.md) · [许可文件](https://github.com/Nasdaq/data-link-python/blob/431094f87292c3c566ddbd647296f65957ac2254/LICENSE.txt) | [EX](../exchanges/README.md) |
| [`openbq-org/OpenBB`](https://github.com/openbq-org/OpenBB) | 读取多供应商的适配层；数据和商业组件权利另查 | 未标记归档；`NOASSERTION`；仅作阅读参考；代码与数据源、企业服务条款独立 | [README](https://github.com/openbq-org/OpenBB/blob/fac2bd450fac5e0b69ca33f11c931f8b1b0b79fa/README.md) · [许可文件](https://github.com/openbq-org/OpenBB/blob/fac2bd450fac5e0b69ca33f11c931f8b1b0b79fa/LICENSE) | [FUND](../funds/README.md) · [IB](../investment-banking/README.md) |
| [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective) | 用自有表格研究交互聚合和数据展示，不是行情供应商 | 未标记归档；`Apache-2.0` | [README](https://github.com/perspective-dev/perspective/blob/d235a268bc424b7d4d2da9b12aa287650e5103a7/README.md) · [许可文件](https://github.com/perspective-dev/perspective/blob/d235a268bc424b7d4d2da9b12aa287650e5103a7/LICENSE.md) | [PE](../private-equity/README.md) · [VC](../venture-capital/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`ranaroussi/yfinance`](https://github.com/ranaroussi/yfinance) | 独立行情研究接口；核对 Yahoo 条款，不推断可商用或可分发 | 未标记归档；`Apache-2.0`；仅作阅读参考；非 Yahoo 官方，功能和数据使用依各来源条款核对 | [README](https://github.com/ranaroussi/yfinance/blob/2492a853aee975b4f39f230ad763298f039e37ae/README.md) · [许可文件](https://github.com/ranaroussi/yfinance/blob/2492a853aee975b4f39f230ad763298f039e37ae/LICENSE.txt) | — |

## 中国市场数据接口

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`akfamily/akshare`](https://github.com/akfamily/akshare) | 独立中国及跨市场数据接口；每个来源的访问和转发条款单查 | 未标记归档；`MIT`；仅作阅读参考；第三方源的权利独立；不作数据再分发建议 | [README](https://github.com/akfamily/akshare/blob/b0362024e714af4083b4b8806fa1e9cf3a7fe9a9/README.md) · [许可文件](https://github.com/akfamily/akshare/blob/b0362024e714af4083b4b8806fa1e9cf3a7fe9a9/LICENSE) | — |
| [`waditu/tushare`](https://github.com/waditu/tushare) | 中国证券数据接口；账号、积分和数据使用权不随源代码获得 | 未标记归档；`BSD-3-Clause`；仅作阅读参考；代码许可不覆盖 Tushare 数据服务、账户和积分 | [README](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/README.md) · [许可文件](https://github.com/waditu/tushare/blob/093856995af0811d3ebbe8c179b8febf4ae706f0/LICENSE) | — |

## 商业数据服务与独立封装

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`jpmorganchase/dataquery-sdk`](https://github.com/jpmorganchase/dataquery-sdk) | 公开客户端与授权数据集分列，不调用服务 | 未标记归档；`Apache-2.0` | [README](https://github.com/jpmorganchase/dataquery-sdk/blob/bdf378f3b5b0b94df928bd9ccdbfcf748412e544/README.md) · [许可文件](https://github.com/jpmorganchase/dataquery-sdk/blob/bdf378f3b5b0b94df928bd9ccdbfcf748412e544/LICENSE) | [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |
| [`jpmorganchase/fusion`](https://github.com/jpmorganchase/fusion) | 公开 SDK 的授权数据发现及访问边界 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/jpmorganchase/fusion/blob/a0d6e547f7adcaeeaddf7b96fdc0d0efe50a2491/README.md) · [许可文件](https://github.com/jpmorganchase/fusion/blob/a0d6e547f7adcaeeaddf7b96fdc0d0efe50a2491/LICENSE) | [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |
| [`LSEG-API-Samples/Example.DataLibrary.Python`](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python) | LSEG 数据库示例；要求服务授权，示例许可不含新闻与行情 | 未标记归档；`Apache-2.0`；仅作阅读参考；官方样例的许可不授予 LSEG 数据订阅 | [README](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python/blob/efba8aebd01900fd53ddf5fb13d1a0935089e101/README.md) · [许可文件](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python/blob/efba8aebd01900fd53ddf5fb13d1a0935089e101/LICENSE) | — |
| [`matthewgilbert/blp`](https://github.com/matthewgilbert/blp) | 独立 Bloomberg API 封装；适用 Bloomberg SDK 与数据条款 | 未标记归档；`Apache-2.0`；仅作阅读参考；第三方封装；必须持有 Bloomberg SDK、账户和数据权限 | [README](https://github.com/matthewgilbert/blp/blob/4716815620cbd989900dd226af97cb6fdc24f068/README.md) · [许可文件](https://github.com/matthewgilbert/blp/blob/4716815620cbd989900dd226af97cb6fdc24f068/LICENSE) | — |
| [`underloam/xbbg`](https://github.com/underloam/xbbg) | 独立 Bloomberg 封装；仍需合法终端或数据服务权限 | 未标记归档；`Apache-2.0`；仅作阅读参考；第三方封装；必须持有 Bloomberg SDK、账户和数据权限 | [README](https://github.com/underloam/xbbg/blob/2ee9171f7dee7abe370e1dbd32d55bd662b47e85/README.md) · [许可文件](https://github.com/underloam/xbbg/blob/2ee9171f7dee7abe370e1dbd32d55bd662b47e85/LICENSE) | — |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
