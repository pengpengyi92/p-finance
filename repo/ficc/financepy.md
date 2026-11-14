# FinancePy — 从 Python 读懂债券与曲线

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/domokane/FinancePy) · [Pinned README](https://github.com/domokane/FinancePy/blob/0b0dc17ab3bcdaa0a21ae73b734f2641c9e5cf41/README.md) · [License](https://github.com/domokane/FinancePy/blob/0b0dc17ab3bcdaa0a21ae73b734f2641c9e5cf41/LICENSE).

来源提交：`0b0dc17ab3bcdaa0a21ae73b734f2641c9e5cf41`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

Python 固定收益、衍生品估值与风险分析；适合从可读的单产品代码、样例和单元测试入手，建立曲线/现金流直觉。

## 先读

1. [Discount curve](https://github.com/domokane/FinancePy/blob/0b0dc17ab3bcdaa0a21ae73b734f2641c9e5cf41/financepy/market/curves/discount_curve.py)：时间容器、折现/零利率接口。
2. [Bond futures](https://github.com/domokane/FinancePy/blob/0b0dc17ab3bcdaa0a21ae73b734f2641c9e5cf41/financepy/products/bonds/bond_future.py)：交割、券息和 implied repo。
3. [曲线示例](https://github.com/domokane/FinancePy/blob/0b0dc17ab3bcdaa0a21ae73b734f2641c9e5cf41/examples/scripts/market/example_discount_curve.py)：跟随合成输入，不先连接真实数据商。

## 练习（未执行）

先验证 list/tuple/array 的时间输入一致性，再用虚构券息与交割日手算 coupon-to-delivery 再投资天数。比较 clean/dirty price、accrual、日计数和年化口径，不能只比较最终小数。

## Our public contribution

[#450](https://github.com/domokane/FinancePy/pull/450) 时间容器校验、[#451](https://github.com/domokane/FinancePy/pull/451) 债券期货 implied repo 均 **OPEN**。本轮只是读取状态，没有重跑历史的曲线或债券测试。

## Boundaries

README 声明 GPL-3.0-or-later；GitHub 自动信号为 GPL-3.0。研究、修改、分发和与其他项目组合时各自核对义务，不自动复制进不同许可的项目。没有真实交易可用性或策略收益声明。

[返回 FICC 路线](README.md) · [Repo 总目录](../README.md)
