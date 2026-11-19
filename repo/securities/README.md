# Securities / 券商与证券

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 14 个公开仓库。

区分券商接入、交易协议、策略模拟及交易后流程。不发实盘指令。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 用虚拟订单测试乱序、拒绝、部分成交和撤销；核对网关重连与事件回放。

## 券商 SDK 与交易接口

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`alpacahq/alpaca-py`](https://github.com/alpacahq/alpaca-py) | 分辨市场数据、交易及模拟环境客户端；不调用实盘 | 未标记归档；`Apache-2.0` | [README](https://github.com/alpacahq/alpaca-py/blob/f8fd9555ec182ccc0f8f6b5b819779fe7b2fb6d3/README.md) · [许可文件](https://github.com/alpacahq/alpaca-py/blob/f8fd9555ec182ccc0f8f6b5b819779fe7b2fb6d3/LICENSE) | [AC](../asset-custody/README.md) |
| [`ib-api-reloaded/ib_async`](https://github.com/ib-api-reloaded/ib_async) | 以只读或模拟流程读券商账户与订单状态机；不下单 | 未标记归档；`BSD-2-Clause` | [README](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/README.md) · [许可文件](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/LICENSE) | [AC](../asset-custody/README.md) |
| [`QuantBox/XAPI3`](https://github.com/QuantBox/XAPI3) | 对比国内市场交易接口抽象；驱动许可与实盘账户另核 | 未标记归档；`BSD-2-Clause`；仅作阅读参考；柜台接口及第三方驱动许可另查 | [README](https://github.com/QuantBox/XAPI3/blob/f99c0f133eddf66531a9a9b38da29c72d5735a9d/README.md) · [许可文件](https://github.com/QuantBox/XAPI3/blob/f99c0f133eddf66531a9a9b38da29c72d5735a9d/LICENSE) | — |
| [`vnpy/vnpy`](https://github.com/vnpy/vnpy) | 读事件驱动交易系统、网关与模拟模式；实盘适配独立审查 | 未标记归档；`MIT` | [README](https://github.com/vnpy/vnpy/blob/c6e231caf32b7fc97e6459817fff66458cf7e7c4/README.md) · [许可文件](https://github.com/vnpy/vnpy/blob/c6e231caf32b7fc97e6459817fff66458cf7e7c4/LICENSE) | — |

## FIX 与交易后事件

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`connamara/quickfixn`](https://github.com/connamara/quickfixn) | 对比 FIX 会话序列号、重发与拒绝路径的 .NET 实现 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/connamara/quickfixn/blob/e3844fbff10b231045a1ad841bde5755bdfd6243/README.md) · [许可文件](https://github.com/connamara/quickfixn/blob/e3844fbff10b231045a1ad841bde5755bdfd6243/LICENSE) | [EX](../exchanges/README.md) |
| [`finos/common-domain-model`](https://github.com/finos/common-domain-model) | 按生命周期研究证券及衍生品事件，不是路由系统 | 未标记归档；`NOASSERTION`；仅作阅读参考；标准、代码及依赖的条款分别核对 | [README](https://github.com/finos/common-domain-model/blob/9f0d6d88913b0ea0aa2413cfde25fd1f5e72889a/README.md) · [许可文件](https://github.com/finos/common-domain-model/blob/9f0d6d88913b0ea0aa2413cfde25fd1f5e72889a/LICENSE.md) | [EX](../exchanges/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) · [AC](../asset-custody/README.md) |
| [`OpenFIGI/api-examples`](https://github.com/OpenFIGI/api-examples) | 核对股票标识映射的歧义、市场及证券类别 | 未标记归档；`Apache-2.0` | [README](https://github.com/OpenFIGI/api-examples/blob/56a0f365185f6ef42d0190407470f76d216b8a55/README.md) · [许可文件](https://github.com/OpenFIGI/api-examples/blob/56a0f365185f6ef42d0190407470f76d216b8a55/LICENSE) | [DATA](../financial-data/README.md) · [AC](../asset-custody/README.md) |
| [`quickfix-j/quickfixj`](https://github.com/quickfix-j/quickfixj) | 用 Java 工具研究订单状态及 FIX 会话 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/quickfix-j/quickfixj/blob/5076f87ea21060446d0afa4ed9c08ce91a4e1e37/README.md) · [许可文件](https://github.com/quickfix-j/quickfixj/blob/5076f87ea21060446d0afa4ed9c08ce91a4e1e37/LICENSE) | [EX](../exchanges/README.md) · [FICC](../ficc/catalog.md) |
| [`quickfix/quickfix`](https://github.com/quickfix/quickfix) | 证券订单消息的会话、回执与重连机制 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/quickfix/quickfix/blob/386ce46e917ae494ab6e90b1be90fd421cdbe3f9/README.md) · [许可文件](https://github.com/quickfix/quickfix/blob/386ce46e917ae494ab6e90b1be90fd421cdbe3f9/LICENSE) | [EX](../exchanges/README.md) · [IB](../investment-banking/README.md) · [FICC](../ficc/catalog.md) · [AC](../asset-custody/README.md) |

## 回测、交易日历和虚拟成交

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`jpmorganchase/abides-jpmc-public`](https://github.com/jpmorganchase/abides-jpmc-public) | 用合成代理研究订单执行、延迟与成交轨迹 | GitHub 已归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/README.md) · [许可文件](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/LICENSE) | [EX](../exchanges/README.md) · [IB](../investment-banking/README.md) |
| [`kernc/backtesting.py`](https://github.com/kernc/backtesting.py) | 用透明的例子核对交易信号到虚拟成交的规则 | 未标记归档；`AGPL-3.0` | [README](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/README.md) · [许可文件](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/LICENSE.md) | [FUND](../funds/README.md) |
| [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader) | 核对订单生命周期处理与仿真/实盘界限 | 未标记归档；`LGPL-3.0` | [README](https://github.com/nautechsystems/nautilus_trader/blob/75122d498aad7d1883c11956962e8fa34a1e3931/README.md) · [许可文件](https://github.com/nautechsystems/nautilus_trader/blob/75122d498aad7d1883c11956962e8fa34a1e3931/LICENSE) | [EX](../exchanges/README.md) · [FUND](../funds/README.md) · [FICC](../ficc/catalog.md) |
| [`QuantConnect/Lean`](https://github.com/QuantConnect/Lean) | 研究虚拟订单和券商模型抽象，禁用实盘 | 未标记归档；`Apache-2.0` | [README](https://github.com/QuantConnect/Lean/blob/f62b677be4f3981e8f6e3eccb31e96d5d51a5043/readme.md) · [许可文件](https://github.com/QuantConnect/Lean/blob/f62b677be4f3981e8f6e3eccb31e96d5d51a5043/LICENSE) | [FUND](../funds/README.md) · [FICC](../ficc/catalog.md) |
| [`stefan-jansen/zipline-reloaded`](https://github.com/stefan-jansen/zipline-reloaded) | 按交易日历复查模拟订单的时间和成交条件 | 未标记归档；`Apache-2.0`；公开 fork | [README](https://github.com/stefan-jansen/zipline-reloaded/blob/5dd9fef5d42c2d084021b5ae10454de166cc5541/README.md) · [许可文件](https://github.com/stefan-jansen/zipline-reloaded/blob/5dd9fef5d42c2d084021b5ae10454de166cc5541/LICENSE) | [FUND](../funds/README.md) |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
