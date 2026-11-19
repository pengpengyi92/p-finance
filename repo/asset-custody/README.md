# Asset Custody / 资产托管与证券服务

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 33 个公开仓库。

传统证券托管的核心是持有记录、证券及现金对账、交收与公司行动。本专题把其消息和运营工具与数字资产/代币化原型分列，不把钱包、节点、交易 SDK 或合约称为银行托管平台。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [本专题讨论 #14](https://github.com/pengpengyi92/p-finance/discussions/14)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 对照 [DTCC Custody Services](https://www.dtcc.com/products-and-services/asset-services/securities-processing/custody-service) 和 [Swift Securities Market Infrastructure](https://www.swift.com/securities/securities-market-infrastructure) 了解业务边界；它们是官方业务来源，不作为开源仓库计数。 [GLEIF API](https://www.gleif.org/en/lei-data/gleif-api) 用于法人标识参考，不是持仓源。
- 以合成证券持仓、现金腿、交收状态、股息或拆股做日终对账；负例包括重复交收、部分交收、金额差、重复分派和错过记录日。清算、交收、托管和标识映射不能互相替代。
- 先读传统消息条目，再选 DvP 的原型作为对照。归档项目只读史料；不处理 KYC、账户凭证、托管密钥、真实指令或第三方资产。

## 传统托管：证券报文、标识和交收接口参考

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`alpacahq/alpaca-py`](https://github.com/alpacahq/alpaca-py) | 券商 SDK 可读账户/持仓/活动；非证券托管实现，不连接账户 | 未标记归档；`Apache-2.0` | [README](https://github.com/alpacahq/alpaca-py/blob/f8fd9555ec182ccc0f8f6b5b819779fe7b2fb6d3/README.md) · [许可文件](https://github.com/alpacahq/alpaca-py/blob/f8fd9555ec182ccc0f8f6b5b819779fe7b2fb6d3/LICENSE) | [SEC](../securities/README.md) |
| [`csingley/ofxtools`](https://github.com/csingley/ofxtools) | OFX 投资交易、持仓与账户报表解析；非 Swift 交收指令 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/csingley/ofxtools/blob/95015fb9dd01c90f5784e3916451eae67c30bc3b/README.rst) · [许可文件](https://github.com/csingley/ofxtools/blob/95015fb9dd01c90f5784e3916451eae67c30bc3b/LICENSE) | — |
| [`ib-api-reloaded/ib_async`](https://github.com/ib-api-reloaded/ib_async) | 券商接口可用于阅读仓位和事件；非托管实现，不连接账户 | 未标记归档；`BSD-2-Clause` | [README](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/README.md) · [许可文件](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/LICENSE) | [SEC](../securities/README.md) |
| [`moov-io/fedwire20022`](https://github.com/moov-io/fedwire20022) | 只作现金腿格式参考，不是 Fedwire Securities 接入 | 未标记归档；`Apache-2.0` | [README](https://github.com/moov-io/fedwire20022/blob/fb2187dff1fa6579f08eccbf58c33970161f8726/README.md) · [许可文件](https://github.com/moov-io/fedwire20022/blob/fb2187dff1fa6579f08eccbf58c33970161f8726/LICENSE) | [CB](../corporate-banking/README.md) |
| [`Open-Cap-Table-Coalition/Open-Cap-Format-OCF`](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | 私有公司股权记录交换，不是法定登记或托管 | 未标记归档；`NOASSERTION`；仅作阅读参考；规范与代码组件适用不同条件 | [固定源码树](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/tree/fd260852ebd3d3e1a3183f8c97ae3f645dc9f0d6) · [许可文件](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/blob/fd260852ebd3d3e1a3183f8c97ae3f645dc9f0d6/LICENSE.md) | [PE](../private-equity/README.md) · [VC](../venture-capital/README.md) · [IB](../investment-banking/README.md) |
| [`OpenFIGI/api-examples`](https://github.com/OpenFIGI/api-examples) | FIGI 标识映射示例；不是证券持仓记录 | 未标记归档；`Apache-2.0` | [README](https://github.com/OpenFIGI/api-examples/blob/56a0f365185f6ef42d0190407470f76d216b8a55/README.md) · [许可文件](https://github.com/OpenFIGI/api-examples/blob/56a0f365185f6ef42d0190407470f76d216b8a55/LICENSE) | [SEC](../securities/README.md) · [DATA](../financial-data/README.md) |
| [`prowide/prowide-core`](https://github.com/prowide/prowide-core) | 证券 MT54x 交收、MT535/536 对账、MT56x 公司行动 | 未标记归档；`Apache-2.0` | [README](https://github.com/prowide/prowide-core/blob/34514beab84c9f9fa134c9f9b0e05e340e38de87/README.md) · [许可文件](https://github.com/prowide/prowide-core/blob/34514beab84c9f9fa134c9f9b0e05e340e38de87/LICENSE.txt) | [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`prowide/prowide-iso20022`](https://github.com/prowide/prowide-iso20022) | sese 交收、semt 持仓报表与 seev 公司行动 | 未标记归档；`Apache-2.0` | [README](https://github.com/prowide/prowide-iso20022/blob/18723858561ed3e7e8f3cf4dc26f1e0cdefc3496/README.md) · [许可文件](https://github.com/prowide/prowide-iso20022/blob/18723858561ed3e7e8f3cf4dc26f1e0cdefc3496/LICENSE.txt) | [CB](../corporate-banking/README.md) |
| [`quickfix/quickfix`](https://github.com/quickfix/quickfix) | 参考确认和分配边界，不等于交收 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/quickfix/quickfix/blob/386ce46e917ae494ab6e90b1be90fd421cdbe3f9/README.md) · [许可文件](https://github.com/quickfix/quickfix/blob/386ce46e917ae494ab6e90b1be90fd421cdbe3f9/LICENSE) | [SEC](../securities/README.md) · [EX](../exchanges/README.md) · [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |

## 传统托管：持仓、基金会计、NAV 与对账参照

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`beancount/beancount`](https://github.com/beancount/beancount) | 用合成仓位、现金与股息核对分录；非中央存管系统 | 未标记归档；`GPL-2.0` | [README](https://github.com/beancount/beancount/blob/9747213802acb733ce53acc6e963f5961f47d6cd/README.rst) · [许可文件](https://github.com/beancount/beancount/blob/9747213802acb733ce53acc6e963f5961f47d6cd/COPYING) | [WM](../wealth-management/README.md) |
| [`formancehq/ledger`](https://github.com/formancehq/ledger) | 模拟券款分录，不是托管头寸主账 | 未标记归档；`MIT` | [README](https://github.com/formancehq/ledger/blob/9ebfa33ceda8a83001e20fad98648161d3740dc2/README.md) · [许可文件](https://github.com/formancehq/ledger/blob/9ebfa33ceda8a83001e20fad98648161d3740dc2/LICENSE) | [FUND](../funds/README.md) · [CB](../corporate-banking/README.md) |
| [`Gnucash/gnucash`](https://github.com/Gnucash/gnucash) | 多币种账簿及证券事件的对账参照 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/Gnucash/gnucash/blob/7574033d1268783c99b87cbb912236bb124861cc/README) · [许可文件](https://github.com/Gnucash/gnucash/blob/7574033d1268783c99b87cbb912236bb124861cc/LICENSE) | [WM](../wealth-management/README.md) |
| [`ildrm/madar-investment-operations-platform`](https://github.com/ildrm/madar-investment-operations-platform) | 基金会计、NAV 和对账的项目；未做生产或监管验收 | 未标记归档；`MIT` | [README](https://github.com/ildrm/madar-investment-operations-platform/blob/42a411ad49ab258fb444aa6968d449d04598bb0f/README.md) · [许可文件](https://github.com/ildrm/madar-investment-operations-platform/blob/42a411ad49ab258fb444aa6968d449d04598bb0f/LICENSE) | [PE](../private-equity/README.md) · [FUND](../funds/README.md) |
| [`ledger/ledger`](https://github.com/ledger/ledger) | 用于合成券、款和分录核对的通用复式账簿 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/ledger/ledger/blob/fe58299d2e8c2c39c4f263f9eae6c667cdcc149f/README.md) · [许可文件](https://github.com/ledger/ledger/blob/fe58299d2e8c2c39c4f263f9eae6c667cdcc149f/LICENSE.md) | — |
| [`portfolio-performance/portfolio`](https://github.com/portfolio-performance/portfolio) | 组合仓位与派息记录参考，不提供托管账户授权 | 未标记归档；`EPL-1.0` | [README](https://github.com/portfolio-performance/portfolio/blob/7a47fcee9d683bbf42a0f262036d90c9a51e71fc/README.md) · [许可文件](https://github.com/portfolio-performance/portfolio/blob/7a47fcee9d683bbf42a0f262036d90c9a51e71fc/LICENSE) | [WM](../wealth-management/README.md) · [FUND](../funds/README.md) |

## 证券融资和交易生命周期

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`finos/common-domain-model`](https://github.com/finos/common-domain-model) | 抵押品和结算事件，不是托管账簿 | 未标记归档；`NOASSERTION`；仅作阅读参考；标准、代码及依赖的条款分别核对 | [README](https://github.com/finos/common-domain-model/blob/9f0d6d88913b0ea0aa2413cfde25fd1f5e72889a/README.md) · [许可文件](https://github.com/finos/common-domain-model/blob/9f0d6d88913b0ea0aa2413cfde25fd1f5e72889a/LICENSE.md) | [SEC](../securities/README.md) · [EX](../exchanges/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |
| [`tradingtechnologies/Strata`](https://github.com/tradingtechnologies/Strata) | 参考券款结算日期与现金流，不发送指令 | 未标记归档；`Apache-2.0` | [README](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/README.md) · [许可文件](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/LICENSE.txt) | [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |
| [`yellowbean/AbsBox`](https://github.com/yellowbean/AbsBox) | 比较预期分派与入账，不执行托管 | 未标记归档；`Apache-2.0` | [README](https://github.com/yellowbean/AbsBox/blob/8afe37485051f357a84c6325556d8472fbca00af/README.md) · [许可文件](https://github.com/yellowbean/AbsBox/blob/8afe37485051f357a84c6325556d8472fbca00af/LICENSE) | [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |

## 独立参考：代币化、跨账本交收与数字资产工具

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`besu-eth/besu`](https://github.com/besu-eth/besu) | 代币化实验的以太坊基础设施；不是证券资产服务 | 未标记归档；`Apache-2.0` | [README](https://github.com/besu-eth/besu/blob/35595d1940787e6f83ae9a091c5b14d54d0643ca/README.md) · [许可文件](https://github.com/besu-eth/besu/blob/35595d1940787e6f83ae9a091c5b14d54d0643ca/LICENSE) | — |
| [`CMTA/CMTAT`](https://github.com/CMTA/CMTAT) | 发行、暂停、权限和资产事件的代币实现；不是传统监管托管 | 未标记归档；`MPL-2.0` | [README](https://github.com/CMTA/CMTAT/blob/08b4fd02d2704ce424418325ef56fa556bf193c9/README.md) · [许可文件](https://github.com/CMTA/CMTAT/blob/08b4fd02d2704ce424418325ef56fa556bf193c9/LICENSE.md) | [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) |
| [`coinbase/coinbase-sdk-nodejs`](https://github.com/coinbase/coinbase-sdk-nodejs) | 数字资产开发接口样例；客户资产和密钥仍受独立控制 | 未标记归档；`NOASSERTION`；仅作阅读参考；只读 SDK 示例；平台及账户权利独立 | [README](https://github.com/coinbase/coinbase-sdk-nodejs/blob/31b3dfe36db28ad712e21dd5421a247f4a532a51/README.md) · [许可文件](https://github.com/coinbase/coinbase-sdk-nodejs/blob/31b3dfe36db28ad712e21dd5421a247f4a532a51/LICENSE.md) | — |
| [`Deed3Labs/Protocol-Contracts`](https://github.com/Deed3Labs/Protocol-Contracts) | 证券型代币与链上信用研究原型；非法律确权或受监管资产托管 | 未标记归档；`AGPL-3.0` | [README](https://github.com/Deed3Labs/Protocol-Contracts/blob/31b705f0a0eb273eb89b7528cd3ae109f535fe1e/README.md) · [许可文件](https://github.com/Deed3Labs/Protocol-Contracts/blob/31b705f0a0eb273eb89b7528cd3ae109f535fe1e/LICENSE) | — |
| [`digital-asset/canton`](https://github.com/digital-asset/canton) | 同步器与权限式账本；非监管托管产品 | 未标记归档；`Apache-2.0` | [README](https://github.com/digital-asset/canton/blob/53625856fac791672754f4bbe308f799172d695c/README.md) · [许可文件](https://github.com/digital-asset/canton/blob/53625856fac791672754f4bbe308f799172d695c/LICENSE.txt) | — |
| [`digital-asset/daml`](https://github.com/digital-asset/daml) | 合约权限、观察者与账本 API；非托管业务实现 | 未标记归档；`Apache-2.0` | [README](https://github.com/digital-asset/daml/blob/1a49987f4136ed5352da8495dbbaf8e755428c32/README.md) · [许可文件](https://github.com/digital-asset/daml/blob/1a49987f4136ed5352da8495dbbaf8e755428c32/LICENSE) | — |
| [`digital-asset/daml-finance`](https://github.com/digital-asset/daml-finance) | 资产、持仓、交收流程的合约库，不是实盘托管 | 未标记归档；`Apache-2.0` | [README](https://github.com/digital-asset/daml-finance/blob/5ba1463ba09a9bdc9267a25ae135b25900351121/README.md) · [许可文件](https://github.com/digital-asset/daml-finance/blob/5ba1463ba09a9bdc9267a25ae135b25900351121/LICENSE) | [FICC](../ficc/catalog.md) |
| [`ethereum/ERCs`](https://github.com/ethereum/ERCs) | 数字资产标准示例；各文件条款与业务用途分别核对 | 未标记归档；`CC0-1.0` | [README](https://github.com/ethereum/ERCs/blob/7214b2237b8a95c885b8fc7306e51fcc1df36562/README.md) · [许可文件](https://github.com/ethereum/ERCs/blob/7214b2237b8a95c885b8fc7306e51fcc1df36562/LICENSE.md) | — |
| [`fireblocks/ts-sdk`](https://github.com/fireblocks/ts-sdk) | 数字资产服务的客户端；不是密钥托管实现 | 未标记归档；`MIT` | [README](https://github.com/fireblocks/ts-sdk/blob/f796b37fd722787466daebb10705ab9e4f3ca5d7/README.md) · [许可文件](https://github.com/fireblocks/ts-sdk/blob/f796b37fd722787466daebb10705ab9e4f3ca5d7/LICENSE) | — |
| [`hyperledger-cacti/cacti`](https://github.com/hyperledger-cacti/cacti) | 异构账本互操作；不等同证券 CSD | 未标记归档；`Apache-2.0` | [README](https://github.com/hyperledger-cacti/cacti/blob/a172a0c6286f5c7d4feb271edacce86c2b02c887/README.md) · [许可文件](https://github.com/hyperledger-cacti/cacti/blob/a172a0c6286f5c7d4feb271edacce86c2b02c887/LICENSE) | — |
| [`hyperledger-labs/harmonia`](https://github.com/hyperledger-labs/harmonia) | 跨账本条件交收与防重放研究 | GitHub 已归档；`Apache-2.0`；仅作阅读参考 | [README](https://github.com/hyperledger-labs/harmonia/blob/c0daddabc47dd991357c160795954b13db4aeec6/README.md) · [许可文件](https://github.com/hyperledger-labs/harmonia/blob/c0daddabc47dd991357c160795954b13db4aeec6/LICENSE) | [FICC](../ficc/catalog.md) |
| [`hyperledger-labs/weaver-dlt-interoperability`](https://github.com/hyperledger-labs/weaver-dlt-interoperability) | 历史跨账本状态证明与交收参考 | GitHub 已归档；`Apache-2.0`；仅作阅读参考 | [README](https://github.com/hyperledger-labs/weaver-dlt-interoperability/blob/59feaff1522e64bcc95e6a88aa670320d792643c/README.md) · [许可文件](https://github.com/hyperledger-labs/weaver-dlt-interoperability/blob/59feaff1522e64bcc95e6a88aa670320d792643c/LICENSE) | — |
| [`jpmorganchase/PADL`](https://github.com/jpmorganchase/PADL) | 隐私账本与权益记录样例；非 JPMorgan 托管服务 | 未标记归档；`Apache-2.0` | [README](https://github.com/jpmorganchase/PADL/blob/3dcab606e81802b305c54b151769850636999957/README.md) · [许可文件](https://github.com/jpmorganchase/PADL/blob/3dcab606e81802b305c54b151769850636999957/LICENSE.txt) | [CB](../corporate-banking/README.md) |
| [`OpenZeppelin/openzeppelin-contracts`](https://github.com/OpenZeppelin/openzeppelin-contracts) | 数字资产通用合约组件；不代表实际托管承诺 | 未标记归档；`MIT` | [README](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/7ee8e000e9c534cbb055895731808c6cc679cb18/README.md) · [许可文件](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/7ee8e000e9c534cbb055895731808c6cc679cb18/LICENSE) | — |
| [`safe-fndn/safe-smart-account`](https://github.com/safe-fndn/safe-smart-account) | 多签合约和链上权限控制示例；不等同传统托管 | 未标记归档；`LGPL-3.0` | [README](https://github.com/safe-fndn/safe-smart-account/blob/247b8ce3bdbf204a120e77f5b369d137424ddc58/README.md) · [许可文件](https://github.com/safe-fndn/safe-smart-account/blob/247b8ce3bdbf204a120e77f5b369d137424ddc58/LICENSE) | — |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [本专题讨论 #14](https://github.com/pengpengyi92/p-finance/discussions/14) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
