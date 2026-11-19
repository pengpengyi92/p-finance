# Venture Capital / 创业投资

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 12 个公开仓库。

区分初创企业股权管理、尽调和融资材料，开源工具不是项目质量或投资评分。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 固定虚拟持有人和两轮融资，比较新股、期权池、转换和总持股比例。

## Cap table、稀释与轮次

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`captableinc/captable`](https://github.com/captableinc/captable) | 以虚拟轮次研究初创股权台账，不写入真实股东 | 未标记归档；`AGPL-3.0` | [README](https://github.com/captableinc/captable/blob/b63006f7bd998a2b4a95b277589e402a6726bd3a/README.md) · [许可文件](https://github.com/captableinc/captable/blob/b63006f7bd998a2b4a95b277589e402a6726bd3a/LICENSE) | [PE](../private-equity/README.md) |
| [`captablex/captablex`](https://github.com/captablex/captablex) | 使用虚拟股东、股类和融资轮次对照 OCF 交换及退出瀑布；不保存真实名册 | 未标记归档；`Apache-2.0` | [README](https://github.com/captablex/captablex/blob/f7489ebb117682bdbefbce7cf7e278c9ca5b634c/README.md) · [许可文件](https://github.com/captablex/captablex/blob/f7489ebb117682bdbefbce7cf7e278c9ca5b634c/LICENSE) | [PE](../private-equity/README.md) |
| [`Open-Cap-Table-Coalition/ocx`](https://github.com/Open-Cap-Table-Coalition/ocx) | 用合成股权事件练习 OCF 输入校验和交换 | 未标记归档；`Apache-2.0` | [README](https://github.com/Open-Cap-Table-Coalition/ocx/blob/915bb38ecd012fa0dea2b68150cecc6b3bb8acca/README.md) · [许可文件](https://github.com/Open-Cap-Table-Coalition/ocx/blob/915bb38ecd012fa0dea2b68150cecc6b3bb8acca/LICENSE) | [PE](../private-equity/README.md) |
| [`Open-Cap-Table-Coalition/Open-Cap-Format-OCF`](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | 用虚拟股东与轮次验证 cap table 事件交换和稀释 | 未标记归档；`NOASSERTION`；仅作阅读参考；规范与代码组件适用不同条件 | [固定源码树](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/tree/fd260852ebd3d3e1a3183f8c97ae3f645dc9f0d6) · [许可文件](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/blob/fd260852ebd3d3e1a3183f8c97ae3f645dc9f0d6/LICENSE.md) | [PE](../private-equity/README.md) · [IB](../investment-banking/README.md) · [AC](../asset-custody/README.md) |

## 企业、股权与信息核对

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`alephdata/aleph`](https://github.com/alephdata/aleph) | 用虚拟公司资料对照检索和实体关联，不把命中当尽调结论 | 未标记归档；`MIT`；仅作阅读参考；工具许可不授予文档或企业记录的二次使用 | [README](https://github.com/alephdata/aleph/blob/fafcc8dfa4384f5d73ab47f84c03e469a91741c2/README.rst) · [许可文件](https://github.com/alephdata/aleph/blob/fafcc8dfa4384f5d73ab47f84c03e469a91741c2/LICENSE.txt) | [PE](../private-equity/README.md) |
| [`EQTPartners/CompanyKG`](https://github.com/EQTPartners/CompanyKG) | 研究企业网络筛选的验证协议，不作为企业质量或融资信号 | 未标记归档；`MIT`；仅作阅读参考；代码许可不授予企业图数据的复用或再分发 | [README](https://github.com/EQTPartners/CompanyKG/blob/e9bf7855c23c0d515d300b2900b33b6155601a01/README.md) · [许可文件](https://github.com/EQTPartners/CompanyKG/blob/e9bf7855c23c0d515d300b2900b33b6155601a01/LICENSE) | [PE](../private-equity/README.md) |
| [`openownership/data-standard`](https://github.com/openownership/data-standard) | 比较公开股权来源的时间、证明材料及冲突 | 未标记归档；`NOASSERTION`；仅作阅读参考；标准文本、实现和数据分别核对 | [README](https://github.com/openownership/data-standard/blob/e8cc3fd7a7fe45c7ad3b542dc07a99847a7960aa/README.md) · [许可文件](https://github.com/openownership/data-standard/blob/e8cc3fd7a7fe45c7ad3b542dc07a99847a7960aa/LICENSE) | [PE](../private-equity/README.md) · [DATA](../financial-data/README.md) |

## 叙事、融资模型及工作流

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`Anexen/pyxirr`](https://github.com/Anexen/pyxirr) | 对虚拟持股轮次与退出现金流做日期敏感性分析 | 未标记归档；`Unlicense` | [README](https://github.com/Anexen/pyxirr/blob/5f31a85684051fb6badb542afba0ac1af5a68f9c/README.md) · [许可文件](https://github.com/Anexen/pyxirr/blob/5f31a85684051fb6badb542afba0ac1af5a68f9c/LICENSE) | [PE](../private-equity/README.md) · [FUND](../funds/README.md) · [IB](../investment-banking/README.md) |
| [`JerBouma/FinanceToolkit`](https://github.com/JerBouma/FinanceToolkit) | 用虚拟报表核对现金流、增长和估值假设 | 未标记归档；`MIT` | [README](https://github.com/JerBouma/FinanceToolkit/blob/245c303efcca5c317c8dcc2fff00d393e1c9ba98/README.md) · [许可文件](https://github.com/JerBouma/FinanceToolkit/blob/245c303efcca5c317c8dcc2fff00d393e1c9ba98/LICENSE.txt) | [PE](../private-equity/README.md) · [FUND](../funds/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`joelparkerhenderson/pitch-deck`](https://github.com/joelparkerhenderson/pitch-deck) | 用公开材料框架设计商业模式和融资叙事的审阅清单，不是投资工具 | 未标记归档；`UNKNOWN`；仅作阅读参考 | [README](https://github.com/joelparkerhenderson/pitch-deck/blob/d44db77068276781049da04b002053cdbdb70de8/README.md) · 许可入口未核实 | — |
| [`numpy/numpy-financial`](https://github.com/numpy/numpy-financial) | 比较投资情景下折现和期内回报；不把等间隔 IRR 当 XIRR | 未标记归档；`BSD-3-Clause` | [README](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/README.md) · [许可文件](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/LICENSE.txt) | [PE](../private-equity/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |
| [`perspective-dev/perspective`](https://github.com/perspective-dev/perspective) | 比较不同虚拟融资轮次的经营指标，不存放标的私有数据 | 未标记归档；`Apache-2.0` | [README](https://github.com/perspective-dev/perspective/blob/d235a268bc424b7d4d2da9b12aa287650e5103a7/README.md) · [许可文件](https://github.com/perspective-dev/perspective/blob/d235a268bc424b7d4d2da9b12aa287650e5103a7/LICENSE.md) | [PE](../private-equity/README.md) · [DATA](../financial-data/README.md) · [CB](../corporate-banking/README.md) · [IB](../investment-banking/README.md) |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
