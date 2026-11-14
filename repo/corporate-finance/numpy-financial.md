# NumPy Financial — 现金流与资金时间价值

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/numpy/numpy-financial) · [Pinned README](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/README.md) · [License](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/LICENSE.txt).

来源提交：`031ed55d322b7aad57311b9d63b589c79df942a1`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

学习 NPV、IRR、付款和利率计算的底层现金流约定。它是数值函数库，不是财报数据库、估值终端或完整信用模型。

## 先读

1. [核心函数](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/numpy_financial/_financial.py)：先看 npv、irr 的输入和时间约定。
2. [函数测试](https://github.com/numpy/numpy-financial/blob/031ed55d322b7aad57311b9d63b589c79df942a1/numpy_financial/tests/test_financial.py)：寻找符号、无解和多解边界。

## 练习（未执行）

构造 t=0 支出和之后三期回款，手算贴现后与函数对照；改变现金流符号，观察 IRR 多根/无根的问题。固定现金流周期和利率周期；非等间隔日期不能直接冒充等周期 NPV/IRR。

## Our public contribution

[#176](https://github.com/numpy/numpy-financial/pull/176) 为 **OPEN**：IRR selector 的类型契约。它是 typing 贡献，不应描述成新 IRR 算法或已合并运行时修复。

## Boundaries

BSD-3-Clause。安装、编译和金融数值实验本轮均 **NOT RUN**。不由类型检查推断实际收益或金融公式全面正确。

[返回公司金融路线](README.md) · [Repo 总目录](../README.md)
