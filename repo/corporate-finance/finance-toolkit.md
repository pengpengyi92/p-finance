# FinanceToolkit — 公司金融模型与财务分析

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/JerBouma/FinanceToolkit) · [Pinned README](https://github.com/JerBouma/FinanceToolkit/blob/375f820d8f84e90e2f42f5d413ed67056cbd4256/README.md) · [License](https://github.com/JerBouma/FinanceToolkit/blob/375f820d8f84e90e2f42f5d413ed67056cbd4256/LICENSE.txt).

来源提交：`375f820d8f84e90e2f42f5d413ed67056cbd4256`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

把财务报表、比率、估值和信用模型连起来看。适合研究 WACC、PVGO、增长与 Merton 模型，但数据源和模型实现应分开审查。

## 先读

1. [WACC 实现](https://github.com/JerBouma/FinanceToolkit/blob/375f820d8f84e90e2f42f5d413ed67056cbd4256/financetoolkit/models/wacc_model.py)：权益/债务权重、税盾和输入形状。
2. [Growth 模型](https://github.com/JerBouma/FinanceToolkit/blob/375f820d8f84e90e2f42f5d413ed67056cbd4256/financetoolkit/models/growth_model.py)：增长、价值分解和无效输入。
3. [WACC 测试](https://github.com/JerBouma/FinanceToolkit/blob/375f820d8f84e90e2f42f5d413ed67056cbd4256/tests/models/test_wacc_model.py)：从一个测试输入追到计算结果，再看接口层。

## 练习（未执行）

用虚构资产负债表手算一个 WACC，再比较 scalar 与带标签序列；检查债务为零、分母为零、EPS 为零和异序时间索引。报告公式、单位、税率假设及输入可得日，不把报表期末当披露日。

## Our public contribution

2026-11-14 官方读回：[#425](https://github.com/JerBouma/FinanceToolkit/pull/425)、[#426](https://github.com/JerBouma/FinanceToolkit/pull/426)、[#427](https://github.com/JerBouma/FinanceToolkit/pull/427)、[#428](https://github.com/JerBouma/FinanceToolkit/pull/428)、[#429](https://github.com/JerBouma/FinanceToolkit/pull/429) 均为 **MERGED**。
这些案例分别适合学习 scalar 契约、校准时域、稀疏索引、无效输入和 as-of 排序。合并不证明所有模型已被独立验证。

## Boundaries

MIT 代码不授予 FinancialModelingPrep 等数据的获取或转售权。优先从纯模型/自带合成输入开始，不自动注册数据服务或启用 MCP。历史 PR 的局部测试不是本轮重跑；经济解释和真实数据准确性 **UNMEASURED**。

[返回公司金融路线](README.md) · [Repo 总目录](../README.md)
