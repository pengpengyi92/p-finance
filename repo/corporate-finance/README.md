# Corporate Finance — 从现金流到企业价值

**Last reviewed:** 2026-11-14 (Asia/Shanghai). 这是阅读与复现实验指引，不是投资建议或已完成的研究实验。

| 顺序 | Repo 档案 | 为什么先看它 | 一个具体问题 |
| --- | --- | --- | --- |
| 1 | [NumPy Financial](numpy-financial.md) | 用最小现金流理解贴现与 IRR | t=0、利率周期、多个 IRR 根怎样处理？ |
| 2 | [FinanceToolkit](finance-toolkit.md) | 把现金流、资本成本、财报比率和估值连接起来 | WACC、PVGO 和增长率如何处理 scalar、缺失值与索引？ |

## 建议路线

1. **先公式**：用三期虚构现金流手算 PV/NPV；写清现金流时点与折现周期。
2. **再模型**：虚构权益、债务、税率和资本成本，手算 WACC。不要先下载整库真实公司数据。
3. **再接口**：对照源码与测试，找 scalar/Series、标签对齐、零分母、无效值和异序日期的行为。
4. **最后真实数据**：只有确认数据权利、调整口径、披露时间、财报修订与缺失处理后，才做真实公司分析。

以上四步都是待执行学习任务，学习收益与经济有效性 **UNMEASURED**。本轮只验证目录及公开贡献状态。

## 读我们的贡献案例

FinanceToolkit [#425–#429](finance-toolkit.md#our-public-contribution) 五条均已合并；NumPy Financial [#176](numpy-financial.md#our-public-contribution) 仍 Open。用一个回归测试理解契约与边界，不把合并状态当成投资能力认证。

## 接到 FICC

企业估值和债券定价都涉及现金流折现，但现金流结构、信用/融资和曲线约定不同。下一站：[FICC 路线](../ficc/README.md)。

[学习记录模板](../HOW_TO_STUDY.md) · [Repo 总目录](../README.md)
