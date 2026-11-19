# Funds & Asset Management / 基金与资产管理

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 20 个公开仓库。

区分组合构建、回测、绩效统计和基金运营。工具不能证明收益或监管适用性。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 先用合成净值、费用和流入流出，分别复核基准、时间加权收益及现金流口径。

## 组合配置与约束

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`cvxgrp/cvxportfolio`](https://github.com/cvxgrp/cvxportfolio) | 研究考虑交易和持有成本的组合优化及回测 | 未标记归档；`GPL-3.0` | [README](https://github.com/cvxgrp/cvxportfolio/blob/351c782b9b8b395c1a5f886b77e0d55f1bc9396e/README.rst) · [许可文件](https://github.com/cvxgrp/cvxportfolio/blob/351c782b9b8b395c1a5f886b77e0d55f1bc9396e/LICENSE) | — |
| [`dcajasn/Riskfolio-Lib`](https://github.com/dcajasn/Riskfolio-Lib) | 在虚拟收益序列上对照风险度量和资产权重约束 | 未标记归档；`BSD-3-Clause` | [README](https://github.com/dcajasn/Riskfolio-Lib/blob/344b899eb72e5636330647f08e3c5d88a8f71a84/README.md) · [许可文件](https://github.com/dcajasn/Riskfolio-Lib/blob/344b899eb72e5636330647f08e3c5d88a8f71a84/LICENSE.txt) | — |
| [`PyPortfolio/PyPortfolioOpt`](https://github.com/PyPortfolio/PyPortfolioOpt) | 用固定协方差与预期收益比较权重、目标和约束 | 未标记归档；`MIT` | [README](https://github.com/PyPortfolio/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/README.md) · [许可文件](https://github.com/PyPortfolio/PyPortfolioOpt/blob/a6638d2e06dae6f444fd022cfd4b3c528902a85b/LICENSE) | [WM](../wealth-management/README.md) |
| [`skfolio/skfolio`](https://github.com/skfolio/skfolio) | 研究组合风险和交叉验证；不能把验证泄漏当超额收益 | 未标记归档；`BSD-3-Clause` | [README](https://github.com/skfolio/skfolio/blob/814170335de993f87eb67f5215ede20f1d956ff1/README.rst) · [许可文件](https://github.com/skfolio/skfolio/blob/814170335de993f87eb67f5215ede20f1d956ff1/LICENSE) | — |

## 绩效与风险报告

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr) | 区分资金加权收益和时间加权收益 | 未标记归档；`Unlicense` | [README](https://github.com/Anexen/pyxirr/blob/5f31a85684051fb6badb542afba0ac1af5a68f9c/README.md) · [许可文件](https://github.com/Anexen/pyxirr/blob/5f31a85684051fb6badb542afba0ac1af5a68f9c/LICENSE) | [PE](../private-equity/README.md) · [VC](../venture-capital/README.md) · [IB](../investment-banking/README.md) |
| [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit) | 比较基本面和组合研究使用的财务字段口径 | 未标记归档；`MIT` | [README](https://github.com/JerBouma/FinanceToolkit/blob/245c303efcca5c317c8dcc2fff00d393e1c9ba98/README.md) · [许可文件](https://github.com/JerBouma/FinanceToolkit/blob/245c303efcca5c317c8dcc2fff00d393e1c9ba98/LICENSE.txt) | [PE](../private-equity/README.md) · [VC](../venture-capital/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`openbq-org/OpenBB`](https://github.com/openbq-org/OpenBB) | 比较研究数据接口的字段一致性和覆盖边界 | 未标记归档；`NOASSERTION`；仅作阅读参考；代码与数据源、企业服务条款独立 | [README](https://github.com/openbq-org/OpenBB/blob/fac2bd450fac5e0b69ca33f11c931f8b1b0b79fa/README.md) · [许可文件](https://github.com/openbq-org/OpenBB/blob/fac2bd450fac5e0b69ca33f11c931f8b1b0b79fa/LICENSE) | [DATA](../financial-data/README.md) · [IB](../investment-banking/README.md) |
| [`pmorissette/ffn`](https://github.com/pmorissette/ffn) | 比较从价格计算的比例收益和组合统计 | 未标记归档；`MIT` | [README](https://github.com/pmorissette/ffn/blob/ab34c72687b6f531ed0cd54ff4cca5c24b6ac988/README.md) · [许可文件](https://github.com/pmorissette/ffn/blob/ab34c72687b6f531ed0cd54ff4cca5c24b6ac988/LICENSE) | — |
| [`portfolio-performance/portfolio`](https://github.com/portfolio-performance/portfolio) | 用合成净值对照时间加权收益与报告口径 | 未标记归档；`EPL-1.0` | [README](https://github.com/portfolio-performance/portfolio/blob/7a47fcee9d683bbf42a0f262036d90c9a51e71fc/README.md) · [许可文件](https://github.com/portfolio-performance/portfolio/blob/7a47fcee9d683bbf42a0f262036d90c9a51e71fc/LICENSE) | [WM](../wealth-management/README.md) · [AC](../asset-custody/README.md) |
| [`ranaroussi/quantstats`](https://github.com/ranaroussi/quantstats) | 从日收益序列生成报告，比较基准、回撤和风险口径 | 未标记归档；`Apache-2.0` | [README](https://github.com/ranaroussi/quantstats/blob/d1a214fb906e76f974f45cdccf923b601c67a756/README.md) · [许可文件](https://github.com/ranaroussi/quantstats/blob/d1a214fb906e76f974f45cdccf923b601c67a756/LICENSE.txt) | — |
| [`stefan-jansen/empyrical-reloaded`](https://github.com/stefan-jansen/empyrical-reloaded) | 用于离线校对收益、回撤及风险统计的定义 | 未标记归档；`Apache-2.0`；公开 fork | [README](https://github.com/stefan-jansen/empyrical-reloaded/blob/f937c0f3ae8edbbe212d4ac7898cdf99f1e7a211/README.md) · [许可文件](https://github.com/stefan-jansen/empyrical-reloaded/blob/f937c0f3ae8edbbe212d4ac7898cdf99f1e7a211/LICENSE) | — |
| [`stefan-jansen/pyfolio-reloaded`](https://github.com/stefan-jansen/pyfolio-reloaded) | 把组合收益、头寸与成交汇总为研究用绩效报告 | 未标记归档；`Apache-2.0`；公开 fork | [README](https://github.com/stefan-jansen/pyfolio-reloaded/blob/7015d68772f4d16a9ad7e01d6787ab4f993d7eef/README.md) · [许可文件](https://github.com/stefan-jansen/pyfolio-reloaded/blob/7015d68772f4d16a9ad7e01d6787ab4f993d7eef/LICENSE) | — |

## 回测与执行假设

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`kernc/backtesting.py`](https://github.com/kernc/backtesting.py) | 在冻结的合成价格上比较回测与基准净值 | 未标记归档；`AGPL-3.0` | [README](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/README.md) · [许可文件](https://github.com/kernc/backtesting.py/blob/ca2e2611621e472542ba90f7243a1fa06a7d7108/LICENSE.md) | [SEC](../securities/README.md) |
| [`nautechsystems/nautilus_trader`](https://github.com/nautechsystems/nautilus_trader) | 研究基于事件的资产组合仿真、成本和执行假设 | 未标记归档；`LGPL-3.0` | [README](https://github.com/nautechsystems/nautilus_trader/blob/75122d498aad7d1883c11956962e8fa34a1e3931/README.md) · [许可文件](https://github.com/nautechsystems/nautilus_trader/blob/75122d498aad7d1883c11956962e8fa34a1e3931/LICENSE) | [SEC](../securities/README.md) · [EX](../exchanges/README.md) · [FICC](../ficc/catalog.md) |
| [`pmorissette/bt`](https://github.com/pmorissette/bt) | 用权重和交易规则构建可审查的策略模拟 | 未标记归档；`MIT` | [README](https://github.com/pmorissette/bt/blob/05230870cefe631e393b194f024d81197e6a51b6/README.md) · [许可文件](https://github.com/pmorissette/bt/blob/05230870cefe631e393b194f024d81197e6a51b6/LICENSE) | — |
| [`polakowo/vectorbt`](https://github.com/polakowo/vectorbt) | 向量化组合模拟读码；公共版与商业条款需分开 | 未标记归档；`NOASSERTION`；仅作阅读参考；公共版许可与商业版/用途限制分别核对 | [README](https://github.com/polakowo/vectorbt/blob/9ac1b697166b00911def494cf95937274218aa54/README.md) · [许可文件](https://github.com/polakowo/vectorbt/blob/9ac1b697166b00911def494cf95937274218aa54/LICENSE.md) | — |
| [`QuantConnect/Lean`](https://github.com/QuantConnect/Lean) | 用固定模拟价格测试组合、费用和执行假设 | 未标记归档；`Apache-2.0` | [README](https://github.com/QuantConnect/Lean/blob/f62b677be4f3981e8f6e3eccb31e96d5d51a5043/readme.md) · [许可文件](https://github.com/QuantConnect/Lean/blob/f62b677be4f3981e8f6e3eccb31e96d5d51a5043/LICENSE) | [SEC](../securities/README.md) · [FICC](../ficc/catalog.md) |
| [`stefan-jansen/zipline-reloaded`](https://github.com/stefan-jansen/zipline-reloaded) | 逐期策略回测与交易成本模型，注意点时数据和退市偏差 | 未标记归档；`Apache-2.0`；公开 fork | [README](https://github.com/stefan-jansen/zipline-reloaded/blob/5dd9fef5d42c2d084021b5ae10454de166cc5541/README.md) · [许可文件](https://github.com/stefan-jansen/zipline-reloaded/blob/5dd9fef5d42c2d084021b5ae10454de166cc5541/LICENSE) | [SEC](../securities/README.md) |

## 投资运营、资本流与账簿

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`formancehq/ledger`](https://github.com/formancehq/ledger) | 演练虚拟结算现金、费用和分账的复式过账 | 未标记归档；`MIT` | [README](https://github.com/formancehq/ledger/blob/9ebfa33ceda8a83001e20fad98648161d3740dc2/README.md) · [许可文件](https://github.com/formancehq/ledger/blob/9ebfa33ceda8a83001e20fad98648161d3740dc2/LICENSE) | [CB](../corporate-banking/README.md) · [AC](../asset-custody/README.md) |
| [`ildrm/madar-investment-operations-platform`](https://github.com/ildrm/madar-investment-operations-platform) | 研究持仓和运营数据工作流，输入和数据模型需独立验证 | 未标记归档；`MIT` | [README](https://github.com/ildrm/madar-investment-operations-platform/blob/42a411ad49ab258fb444aa6968d449d04598bb0f/README.md) · [许可文件](https://github.com/ildrm/madar-investment-operations-platform/blob/42a411ad49ab258fb444aa6968d449d04598bb0f/LICENSE) | [PE](../private-equity/README.md) · [AC](../asset-custody/README.md) |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
