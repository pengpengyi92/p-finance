# Private Equity / 私募股权

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 16 个公开仓库。

从股权结构、交易模型和企业核实入手。区分 GP/LP 账务、企业估值和支持工具。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 用合成对价、债务、退出值与现金流手算桥接及 IRR；写明条款、期间和可见数据。

## 股权与退出分配

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`captableinc/captable`](https://github.com/captableinc/captable) | 读股权台账、持有人和持股变化的产品工作流 | 未标记归档；`AGPL-3.0` | [README](https://github.com/captableinc/captable/blob/b63006f7bd998a2b4a95b277589e402a6726bd3a/README.md) · [许可文件](https://github.com/captableinc/captable/blob/b63006f7bd998a2b4a95b277589e402a6726bd3a/LICENSE) | [VC](../venture-capital/README.md) |
| [`captablex/captablex`](https://github.com/captablex/captablex) | 对照股类、优先权和退出瀑布的工程模型，未验证任何基金条款 | 未标记归档；`Apache-2.0` | [README](https://github.com/captablex/captablex/blob/f7489ebb117682bdbefbce7cf7e278c9ca5b634c/README.md) · [许可文件](https://github.com/captablex/captablex/blob/f7489ebb117682bdbefbce7cf7e278c9ca5b634c/LICENSE) | [VC](../venture-capital/README.md) |
| [`Open-Cap-Table-Coalition/ocx`](https://github.com/Open-Cap-Table-Coalition/ocx) | 查看资本结构事件在 OCF 与内部数据模型之间怎样转换 | 未标记归档；`Apache-2.0` | [README](https://github.com/Open-Cap-Table-Coalition/ocx/blob/915bb38ecd012fa0dea2b68150cecc6b3bb8acca/README.md) · [许可文件](https://github.com/Open-Cap-Table-Coalition/ocx/blob/915bb38ecd012fa0dea2b68150cecc6b3bb8acca/LICENSE) | [VC](../venture-capital/README.md) |
| [`Open-Cap-Table-Coalition/Open-Cap-Format-OCF`](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | 对比持股、证券类别和既有股权事件的交换格式 | 未标记归档；`NOASSERTION`；仅作阅读参考；规范与代码组件适用不同条件 | [固定源码树](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/tree/fd260852ebd3d3e1a3183f8c97ae3f645dc9f0d6) · [许可文件](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/blob/fd260852ebd3d3e1a3183f8c97ae3f645dc9f0d6/LICENSE.md) | [VC](../venture-capital/README.md) · [IB](../investment-banking/README.md) · [AC](../asset-custody/README.md) |

## LBO、估值及基金现金流

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr) | 以合成不规则募集和退出现金流验证 XIRR | 未标记归档；`Unlicense` | [README](https://github.com/Anexen/pyxirr/blob/5f31a85684051fb6badb542afba0ac1af5a68f9c/README.md) · [许可文件](https://github.com/Anexen/pyxirr/blob/5f31a85684051fb6badb542afba0ac1af5a68f9c/LICENSE) | [VC](../venture-capital/README.md) · [FUND](../funds/README.md) · [IB](../investment-banking/README.md) |
| [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit) | 复查财务比率与可比估值输入 | 未标记归档；`MIT` | [README](https://github.com/JerBouma/FinanceToolkit/blob/245c303efcca5c317c8dcc2fff00d393e1c9ba98/README.md) · [许可文件](https://github.com/JerBouma/FinanceToolkit/blob/245c303efcca5c317c8dcc2fff00d393e1c9ba98/LICENSE.txt) | [VC](../venture-capital/README.md) · [FUND](../funds/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`Nachidoestech/lbo-model`](https://github.com/Nachidoestech/lbo-model) | 拆解合成并购融资、债务偿还与退出杠杆 | 未标记归档；`MIT` | [README](https://github.com/Nachidoestech/lbo-model/blob/8efc6b5472f97e5940ffc539b72a9a1f5670e4bf/README.md) · [许可文件](https://github.com/Nachidoestech/lbo-model/blob/8efc6b5472f97e5940ffc539b72a9a1f5670e4bf/LICENSE) | [IB](../investment-banking/README.md) |
| [`numpy/numpy-financial`](https://github.com/numpy/numpy-financial) | 用合成等间隔现金流核对 NPV 与 IRR | 未标记归档；`BSD-3-Clause` | [README](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/README.md) · [许可文件](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/LICENSE.txt) | [VC](../venture-capital/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |

## 尽调、企业与受益所有权

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`alephdata/aleph`](https://github.com/alephdata/aleph) | 研究调查文档检索与交叉引用；关联提示需人工核对 | 未标记归档；`MIT`；仅作阅读参考；工具许可不授予文档或企业记录的二次使用 | [README](https://github.com/alephdata/aleph/blob/fafcc8dfa4384f5d73ab47f84c03e469a91741c2/README.rst) · [许可文件](https://github.com/alephdata/aleph/blob/fafcc8dfa4384f5d73ab47f84c03e469a91741c2/LICENSE.txt) | [VC](../venture-capital/README.md) |
| [`dgunning/edgartools`](https://github.com/dgunning/edgartools) | 追踪尽调财报的申报期和修订 | 未标记归档；`MIT` | [README](https://github.com/dgunning/edgartools/blob/e2cc982e0084fa8e46da78f09493d1767845c8b5/README.md) · [许可文件](https://github.com/dgunning/edgartools/blob/e2cc982e0084fa8e46da78f09493d1767845c8b5/LICENSE.txt) | [DATA](../financial-data/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`EQTPartners/CompanyKG`](https://github.com/EQTPartners/CompanyKG) | 以公开说明研究企业图与相似度任务；单独核查语料再利用条款 | 未标记归档；`MIT`；仅作阅读参考；代码许可不授予企业图数据的复用或再分发 | [README](https://github.com/EQTPartners/CompanyKG/blob/e9bf7855c23c0d515d300b2900b33b6155601a01/README.md) · [许可文件](https://github.com/EQTPartners/CompanyKG/blob/e9bf7855c23c0d515d300b2900b33b6155601a01/LICENSE) | [VC](../venture-capital/README.md) |
| [`openownership/data-standard`](https://github.com/openownership/data-standard) | 用 BODS 的实体、权益人和持有关系建受益所有权核查字段 | 未标记归档；`NOASSERTION`；仅作阅读参考；标准文本、实现和数据分别核对 | [README](https://github.com/openownership/data-standard/blob/e8cc3fd7a7fe45c7ad3b542dc07a99847a7960aa/README.md) · [许可文件](https://github.com/openownership/data-standard/blob/e8cc3fd7a7fe45c7ad3b542dc07a99847a7960aa/LICENSE) | [VC](../venture-capital/README.md) · [DATA](../financial-data/README.md) |
| [`openownership/lib-cove-bods`](https://github.com/openownership/lib-cove-bods) | 校验 BODS 樣例版本、必填字段与非法关系 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/openownership/lib-cove-bods/blob/481a6c2f263722047598ed7ba0870830bd249455/README.md) · [许可文件](https://github.com/openownership/lib-cove-bods/blob/481a6c2f263722047598ed7ba0870830bd249455/LICENSE) | [DATA](../financial-data/README.md) |
| [`opensanctions/yente`](https://github.com/opensanctions/yente) | 用合成人名比较制裁筛查匹配和误报；法律判断与数据授权独立 | 未标记归档；`MIT`；仅作阅读参考；服务代码与筛查数据集授权独立 | [README](https://github.com/opensanctions/yente/blob/7074db814a382971370c5840509c0c9ec69380e1/README.md) · [许可文件](https://github.com/opensanctions/yente/blob/7074db814a382971370c5840509c0c9ec69380e1/LICENSE) | [DATA](../financial-data/README.md) |

## 投后和基金运营

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`ildrm/madar-investment-operations-platform`](https://github.com/ildrm/madar-investment-operations-platform) | 阅读投资运营与可追溯台账架构，不代表 GP 一体化系统 | 未标记归档；`MIT` | [README](https://github.com/ildrm/madar-investment-operations-platform/blob/42a411ad49ab258fb444aa6968d449d04598bb0f/README.md) · [许可文件](https://github.com/ildrm/madar-investment-operations-platform/blob/42a411ad49ab258fb444aa6968d449d04598bb0f/LICENSE) | [FUND](../funds/README.md) · [AC](../asset-custody/README.md) |
| [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective) | 用合成投后指标搭配切片和汇总 | 未标记归档；`Apache-2.0` | [README](https://github.com/perspective-dev/perspective/blob/d235a268bc424b7d4d2da9b12aa287650e5103a7/README.md) · [许可文件](https://github.com/perspective-dev/perspective/blob/d235a268bc424b7d4d2da9b12aa287650e5103a7/LICENSE.md) | [VC](../venture-capital/README.md) · [DATA](../financial-data/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
