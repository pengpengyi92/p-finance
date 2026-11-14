# QuantLib — 固定收益与衍生品基础架构

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/lballabio/QuantLib) · [Pinned README](https://github.com/lballabio/QuantLib/blob/ab984dd7328fbca531262ea0afffd33faeaacdc9/README.md) · [License](https://github.com/lballabio/QuantLib/blob/ab984dd7328fbca531262ea0afffd33faeaacdc9/LICENSE.TXT).

来源提交：`ab984dd7328fbca531262ea0afffd33faeaacdc9`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

研究日期/日历、day count、曲线、现金流、定价引擎和风险量之间的关系。核心仓库是 C++；Python 绑定是另一个安装和版本兼容问题，不能把二者混为一个测试结果。

## 先读

1. [Rate helpers](https://github.com/lballabio/QuantLib/blob/ab984dd7328fbca531262ea0afffd33faeaacdc9/ql/termstructures/yield/ratehelpers.hpp)：市场工具如何进入曲线构造。
2. [Zero curve](https://github.com/lballabio/QuantLib/blob/ab984dd7328fbca531262ea0afffd33faeaacdc9/ql/termstructures/yield/zerocurve.hpp)：节点、插值与利率约定。

## 练习（未执行）

用合成折现因子验证零息现金流 PV，再做平行 1bp bump；记录币种、估值日、day count、复利和结算约定。跨库对照时先统一这些约定，再比较数值，不把不同口径的差异当成 bug。

## Our public contribution

[#3046](https://github.com/lballabio/QuantLib/issues/3046) 是固定 kappa 指数样条系数的 **Issue**，当前 **CLOSED**；不是我们提交的代码 PR。关闭状态本身不说明任何特定修复提交的归属或生产影响。

## Boundaries

上游采用 BSD 风格的 QuantLib 许可；GitHub 自动分类为 NOASSERTION，应阅读原文，不能解释为没有许可。此处没有重建 C++ 主分支、安装 Python 绑定或验证全部曲线模型。

[返回 FICC 路线](README.md) · [Repo 总目录](../README.md)
