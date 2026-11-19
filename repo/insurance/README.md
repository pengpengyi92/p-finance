# Insurance / 保险

**目录更新：** 2026-11-20T00:43:00+08:00（Asia/Shanghai） · **本专题：** 9 个公开仓库。

把模型计算、巨灾工具和理赔业务分开。仅使用虚拟保单和无个人信息的合成损失。

[Repo 总目录](../README.md) · [可展开行业目录](../market-map.md) · [公开来源账本](../finance-topics.json) · [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)

这是已核验的选录，不是全球全集或生产背书。沿用的旧来源不重新标注为当天核验；逐条快照见账本。同一仓库可跨专题，每页解释该用途。

## 起步路线

- 先固定赔付三角和口径，再手算链梯发展因子；巨灾另测模型、暴露、脆弱性及许可来源。

## 精算、寿险和准备金

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`casact/chainladder-python`](https://github.com/casact/chainladder-python) | 检查赔付三角、发展因子和准备金估计的输入假设 | 未标记归档；`MPL-2.0` | [README](https://github.com/casact/chainladder-python/blob/687e329c298eceb66a75cd6c0449658e14f5a328/README.rst) · [许可文件](https://github.com/casact/chainladder-python/blob/687e329c298eceb66a75cd6c0449658e14f5a328/LICENSE) | — |
| [`lifelib-dev/lifelib`](https://github.com/lifelib-dev/lifelib) | 用公开合成情景读寿险现金流、利润测试和模型结构 | 未标记归档；`MIT` | [README](https://github.com/lifelib-dev/lifelib/blob/d44068e2a7c6aecbc14688569b1108e7bfd6a123/README.rst) · [许可文件](https://github.com/lifelib-dev/lifelib/blob/d44068e2a7c6aecbc14688569b1108e7bfd6a123/LICENSE.txt) | — |
| [`mages/ChainLadder`](https://github.com/mages/ChainLadder) | 以 R 复查赔付三角与准备金方法，与 Python 原理对照 | 未标记归档；`UNKNOWN`；仅作阅读参考 | [README](https://github.com/mages/ChainLadder/blob/41f4e949e5c3bffd7a18af2c0eaa98d6bae2da2f/README.md) · 许可入口未核实 | — |

## 巨灾、暴露与再保模拟

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`CLIMADA-project/climada_python`](https://github.com/CLIMADA-project/climada_python) | 研究灾害、暴露、脆弱性和适应策略的模型组合 | 未标记归档；`GPL-3.0` | [README](https://github.com/CLIMADA-project/climada_python/blob/cc0b21516a156384f718e328c59b60138dc1775c/README.md) · [许可文件](https://github.com/CLIMADA-project/climada_python/blob/cc0b21516a156384f718e328c59b60138dc1775c/LICENSE) | — |
| [`OasisLMF/OasisLMF`](https://github.com/OasisLMF/OasisLMF) | 读暴露、灾害和赔付模拟框架；商业模型和风险数据另授权 | 未标记归档；`BSD-3-Clause` | [README](https://github.com/OasisLMF/OasisLMF/blob/d513ce5c1cef0dde06c87aa3713f1a654af4e386/README.md) · [许可文件](https://github.com/OasisLMF/OasisLMF/blob/d513ce5c1cef0dde06c87aa3713f1a654af4e386/LICENSE) | — |
| [`OasisLMF/OasisPiWind`](https://github.com/OasisLMF/OasisPiWind) | 用示例风险模型学习 Oasis 输入与损失流程，不用于真实承保 | 未标记归档；`BSD-2-Clause` | [README](https://github.com/OasisLMF/OasisPiWind/blob/661272420f6c7552a28953b226cf2f029343ac4b/README.md) · [许可文件](https://github.com/OasisLMF/OasisPiWind/blob/661272420f6c7552a28953b226cf2f029343ac4b/LICENSE) | — |

## 保单、理赔及运营

| 规范仓库 | 本专题用途 | 状态 / 许可线索 | 固定来源 | 也见 |
| --- | --- | --- | --- | --- |
| [`openimis/openimis-be-claim_py`](https://github.com/openimis/openimis-be-claim_py) | 读医疗索赔状态和复核模块；仅用虚拟病历 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/openimis/openimis-be-claim_py/blob/77b197ecb4322d99a9268d02766c4e1658999d20/README.md) · [许可文件](https://github.com/openimis/openimis-be-claim_py/blob/77b197ecb4322d99a9268d02766c4e1658999d20/LICENSE.md) | — |
| [`openimis/openimis-be-policy_py`](https://github.com/openimis/openimis-be-policy_py) | 读医疗保险保单状态和缴费关联；不上传被保人数据 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/openimis/openimis-be-policy_py/blob/d4a3df96fea44f91c500d1633695a86f7ba241de/README.md) · [许可文件](https://github.com/openimis/openimis-be-policy_py/blob/d4a3df96fea44f91c500d1633695a86f7ba241de/LICENSE.md) | — |
| [`openimis/openimis-be_py`](https://github.com/openimis/openimis-be_py) | 了解公共卫生保险后台模块、权限和业务扩展，不当商业保险核心 | 未标记归档；`NOASSERTION`；仅作阅读参考 | [README](https://github.com/openimis/openimis-be_py/blob/b30b98944baab2b4be7c45a8be51906b400715eb/README.md) · [许可文件](https://github.com/openimis/openimis-be_py/blob/b30b98944baab2b4be7c45a8be51906b400715eb/LICENSE.md) | — |

## 边界与投稿

许可列为 GitHub 分类线索，不是法律判断。代码、规范、数据、商业 API 及账户资格各自独立。不因所有者是金融机构就推断某个业务部门使用或维护该仓库。未执行第三方代码或验证金融正确性、性能、安全或生产适用性：**NOT_RUN / UNMEASURED**。

欢迎在 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo) 推荐仓库、分享使用经验或复现，也可提交 PR。请提供规范仓库 URL、领域用途、来源和权利限制；跨专题时为每个专题分别写一条具体用途，不用复制整个表。只使用公开、可授权或合成的材料。
