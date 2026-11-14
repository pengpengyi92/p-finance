# ORE — 从曲线定价走向组合风险

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/OpenSourceRisk/Engine) · [Pinned README](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/README.md) · [License](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/license.txt).

来源提交：`3d75a69087911a7e2cf1e6882da7bc27135c0762`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

Open Source Risk Engine：学习市场配置、产品/组合、定价、情景和风险报告如何组成系统。它不是获得实际市场数据授权的捷径。

## 先读

1. [CurveBuilding 示例说明](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/Examples/CurveBuilding/Readme.md)：先理解输入/输出和曲线构造任务。
2. [Yield curve configuration](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/OREData/ored/configuration/yieldcurveconfig.hpp)：把模型选择和市场约定显式化。

## 练习（未执行）

从最小合成曲线配置开始，追踪节点到现金流 PV 再到情景结果；独立用有限差分检查局部敏感度。记录依赖版本、插值/外推、端点处理与报告币种，不把某个扩展库单测当成 ORE 全系统验收。

## Our public contribution

[#377](https://github.com/OpenSourceRisk/Engine/pull/377) 与 [#378](https://github.com/OpenSourceRisk/Engine/pull/378) 均 **OPEN**：分别涉及 coupon 归一化和 flat extrapolation primitive。两条是不同补丁，历史局部测试范围也不同。

## Boundaries

许可为上游 BSD 风格文本，GitHub 信号 NOASSERTION；需读原许可及依赖条款。C++ 构建和组合风险流程较重，本轮未安装、重跑或声明 XVA/生产风险有效性。

[返回 FICC 路线](README.md) · [Repo 总目录](../README.md)
