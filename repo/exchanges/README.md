# Exchange / 交易所

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 15 个公开仓库。

把撮合实验、协议库、交易所数据服务及数字资产接口分列，不推断任何场所生产部署。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 以合成订单流验证价时优先、撤单和部分成交；许可行情和连接权限另核。

## 撮合和订单簿实现

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`enewhuis/liquibook`](https://github.com/enewhuis/liquibook) | 研究限价订单、部分成交和撤单的 C++ 撮合组件 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/enewhuis/liquibook/blob/2427613b32f1667abae68a01df6af9ba8270f8e7/README.md) · [许可文件](https://github.com/enewhuis/liquibook/blob/2427613b32f1667abae68a01df6af9ba8270f8e7/license.txt) | — |
| [`exchange-core/exchange-core`](https://github.com/exchange-core/exchange-core) | 读订单簿、撮合和风险检查的模拟实现，不推断真实场所部署 | 未标记归档；`Apache-2.0` | [README](https://github.com/exchange-core/exchange-core/blob/75d95cd4bce49929b14ed2180300509c7b3d8801/README.md) · [许可文件](https://github.com/exchange-core/exchange-core/blob/75d95cd4bce49929b14ed2180300509c7b3d8801/LICENSE.txt) | — |

## 市场报文与数据分发

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`connamara/quickfixn`](https://github.com/connamara/quickfixn) | 用模拟参与者消息检验顺序与回执，不连接交易所 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/connamara/quickfixn/blob/e3844fbff10b231045a1ad841bde5755bdfd6243/README.md) · [许可文件](https://github.com/connamara/quickfixn/blob/e3844fbff10b231045a1ad841bde5755bdfd6243/LICENSE) | [SEC](../securities/README.md) |
| [`databento/databento-python`](https://github.com/databento/databento-python) | 读逐笔和订单簿数据的解码接口，不复制有权数据 | 未标记归档；`Apache-2.0`；仅作阅读参考；授权市场数据另需协议，不调用服务 | [README](https://github.com/databento/databento-python/blob/f6529f1062e0642fe52334d767a72f2a75244398/README.md) · [许可文件](https://github.com/databento/databento-python/blob/f6529f1062e0642fe52334d767a72f2a75244398/LICENSE) | [DATA](../financial-data/README.md) |
| [`finos/common-domain-model`](https://github.com/finos/common-domain-model) | 阅读交易后生命周期及结算事件的规范表示 | 未标记归档；`NOASSERTION`；仅作阅读参考；标准、代码及依赖的条款分别核对 | [README](https://github.com/finos/common-domain-model/blob/9f0d6d88913b0ea0aa2413cfde25fd1f5e72889a/README.md) · [许可文件](https://github.com/finos/common-domain-model/blob/9f0d6d88913b0ea0aa2413cfde25fd1f5e72889a/LICENSE.md) | [SEC](../securities/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) · [AC](../asset-custody/README.md) |
| [`LMAX-Exchange/disruptor`](https://github.com/LMAX-Exchange/disruptor) | 读取事件分发工程组件；不代表场所交易或撮合系统 | 未标记归档；`Apache-2.0` | [README](https://github.com/LMAX-Exchange/disruptor/blob/c871ca49826a6be7ada6957f6fbafcfecf7b1f87/README.adoc) · [许可文件](https://github.com/LMAX-Exchange/disruptor/blob/c871ca49826a6be7ada6957f6fbafcfecf7b1f87/LICENCE.txt) | [FICC](../ficc/catalog.md) |
| [`quickfix-j/quickfixj`](https://github.com/quickfix-j/quickfixj) | 检查测试场所客户端的心跳、断线和重发行为 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/quickfix-j/quickfixj/blob/5076f87ea21060446d0afa4ed9c08ce91a4e1e37/README.md) · [许可文件](https://github.com/quickfix-j/quickfixj/blob/5076f87ea21060446d0afa4ed9c08ce91a4e1e37/LICENSE) | [SEC](../securities/README.md) · [FICC](../ficc/catalog.md) |
| [`quickfix/quickfix`](https://github.com/quickfix/quickfix) | 模拟参与者和场所之间的 FIX 消息与序列 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/quickfix/quickfix/blob/386ce46e917ae494ab6e90b1be90fd421cdbe3f9/README.md) · [许可文件](https://github.com/quickfix/quickfix/blob/386ce46e917ae494ab6e90b1be90fd421cdbe3f9/LICENSE) | [SEC](../securities/README.md) · [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) · [AC](../asset-custody/README.md) |

## 市场微观结构与回放

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`jpmorganchase/abides-jpmc-public`](https://github.com/jpmorganchase/abides-jpmc-public) | 比较合成市场下撮合与参与者事件回放 | GitHub 已归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/README.md) · [许可文件](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/LICENSE) | [SEC](../securities/README.md) · [IB](../investment-banking/README.md) |
| [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader) | 用虚拟场所适配器对照市场回放事件 | 未标记归档；`LGPL-3.0` | [README](https://github.com/nautechsystems/nautilus_trader/blob/75122d498aad7d1883c11956962e8fa34a1e3931/README.md) · [许可文件](https://github.com/nautechsystems/nautilus_trader/blob/75122d498aad7d1883c11956962e8fa34a1e3931/LICENSE) | [SEC](../securities/README.md) · [FUND](../funds/README.md) · [FICC](../ficc/catalog.md) |

## 证券市场数据服务

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`J-Quants/jquants-api-client-python`](https://github.com/J-Quants/jquants-api-client-python) | 读日本上市证券数据服务的分页和交易日语义，不是撮合引擎 | 未标记归档；`Apache-2.0`；仅作阅读参考；J-Quants 服务条款和订阅权限另核 | [README](https://github.com/J-Quants/jquants-api-client-python/blob/4a6ab360dbd43e763595f7ad362e749a25d6439d/README.md) · [许可文件](https://github.com/J-Quants/jquants-api-client-python/blob/4a6ab360dbd43e763595f7ad362e749a25d6439d/LICENSE) | [DATA](../financial-data/README.md) |
| [`Nasdaq/data-link-python`](https://github.com/Nasdaq/data-link-python) | 交易所品牌数据服务客户端；非交易接入或交易所主系统 | 未标记归档；`MIT`；仅作阅读参考；数据集许可、套餐及再分发限制独立 | [README](https://github.com/Nasdaq/data-link-python/blob/431094f87292c3c566ddbd647296f65957ac2254/README.md) · [许可文件](https://github.com/Nasdaq/data-link-python/blob/431094f87292c3c566ddbd647296f65957ac2254/LICENSE.txt) | [DATA](../financial-data/README.md) |

## 数字资产接口（非传统证券场所）

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`binance/binance-connector-python`](https://github.com/binance/binance-connector-python) | 数字资产场所 REST 和流式接口示例；账户、市场和地区条款另核 | 未标记归档；`MIT`；仅作阅读参考；SDK 许可不授予交易资格或行情转发 | [README](https://github.com/binance/binance-connector-python/blob/621b0062c2596b917e789120c3ebf4ad6cd96471/README.md) · [许可文件](https://github.com/binance/binance-connector-python/blob/621b0062c2596b917e789120c3ebf4ad6cd96471/LICENSE.md) | — |
| [`ccxt/ccxt`](https://github.com/ccxt/ccxt) | 比较不同数字资产交易场所的接口适配，不等同监管交易所或实盘认证 | 未标记归档；`MIT`；仅作阅读参考；接口适配代码不授予任何场所服务或数据权利 | [README](https://github.com/ccxt/ccxt/blob/c7d973187dbe1143a1775ba89e7c8cef3fb241f9/README.md) · [许可文件](https://github.com/ccxt/ccxt/blob/c7d973187dbe1143a1775ba89e7c8cef3fb241f9/LICENSE.txt) | — |
| [`coinbase/coinbase-advanced-py`](https://github.com/coinbase/coinbase-advanced-py) | 数字资产交易场所的官方客户端；不是传统证券交易所实现 | 未标记归档；`Apache-2.0`；仅作阅读参考；SDK、账户和数字资产市场服务分开；只读参考 | [README](https://github.com/coinbase/coinbase-advanced-py/blob/338a4e34f497ff51bd6c61ae440061235dbf8fa9/README.md) · [许可文件](https://github.com/coinbase/coinbase-advanced-py/blob/338a4e34f497ff51bd6c61ae440061235dbf8fa9/LICENSE.md) | — |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
