# FICC — 曲线、定价、风险与系统

**Last reviewed:** 2026-11-14 (Asia/Shanghai). 从可读实现开始，再比较系统架构；不按品牌或星数宣称优劣。

| 层次 | Repo 档案 | 推荐阅读目标 |
| --- | --- | --- |
| Python 单产品 | [FinancePy](financepy.md) | 折现曲线、债券、期货 implied repo；注意 GPL |
| 核心金融库 | [QuantLib](quantlib.md) | 日期/日历、rate helpers、曲线与定价引擎 |
| Java 架构 | [Strata](strata.md) | 产品、市场数据、校准、定价、敏感度分层 |
| 组合风险 | [ORE](ore.md) | 曲线配置、组合输入、情景与风险输出 |
| SDK 与服务 | [GS Quant](gs-quant.md) | instrument/context/provider/result 与数据权限 |
| 权限先行 | [rateslib](rateslib.md) | 只作外部参考；先许可问答，不自动 fork/运行/改写 |

## 两条起步路线

**Python / 曲线路线：** FinancePy → QuantLib 的曲线与日期约定 → 统一口径后做跨实现对照。

**工程 / 风险路线：** QuantLib 的金融对象 → Strata 的分层 → ORE 的组合/情景 → GS Quant 的服务权限边界。不是要求一次安装全部库。

## 第一个同题比较（计划，未执行）

- 仅用合成数据：三个期限的零利率和一组明确日期/时间的固定现金流。
- Baseline：独立手算折现 PV；固定复利、day count、结算日、插值、外推和币种。
- 对照：先检查折现因子与现金流逐项 PV，再检查平行 1bp bump 的 DV01；标明每单位本金还是金额、每 bp 还是每单位利率、风险符号及 bump/recalibration 方式。
- Negative controls：错用百分数/bp、错日期、越界外推、clean/dirty 混淆。必须检测或明确 NOT_IMPLEMENTED。
- 产物：输入/版本/许可清单、预期值、误差容忍、失败日志和限制。数值或速度优劣在实测前 **UNMEASURED**。

这是研究练习规格，目录页不包含声称已执行的跨库 benchmark。任何库的 mock/单测通过也不代表取得真实数据 entitlement 或可生产交易。

## 贡献与许可

详情见各档案：PR、Issue、Discussion 分开登记；Open 不等于接受。rateslib 是 source-available 而非开源，FinancePy 有 copyleft 条件；其余也需读当前许可、第三方依赖与数据条款。

[学习记录模板](../HOW_TO_STUDY.md) · [公司金融路线](../corporate-finance/README.md) · [Repo 总目录](../README.md)
