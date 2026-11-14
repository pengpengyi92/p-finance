# GS Quant — 金融对象、Context 与数据边界

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/goldmansachs/gs-quant) · [Pinned README](https://github.com/goldmansachs/gs-quant/blob/8725ddf2ce4b925a7ce68ba90eca353455ac34b5/README.md) · [License](https://github.com/goldmansachs/gs-quant/blob/8725ddf2ce4b925a7ce68ba90eca353455ac34b5/LICENSE).

来源提交：`8725ddf2ce4b925a7ce68ba90eca353455ac34b5`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

学习面向研究和前台分析的 Python SDK：金融对象、pricing context、风险请求和数据提供方如何衔接。SDK 可读与后端金融服务可用是两回事。

## 先读

1. [Pricing Context 教程](https://github.com/goldmansachs/gs-quant/blob/8725ddf2ce4b925a7ce68ba90eca353455ac34b5/gs_quant/documentation/02_pricing_and_risk/01_scenarios_and_contexts/tutorials/Pricing_Context.ipynb)：先辨别本地对象与需要授权的调用；本轮只核对路径，未运行 notebook。
2. [FRED data 适配器](https://github.com/goldmansachs/gs-quant/blob/8725ddf2ce4b925a7ce68ba90eca353455ac34b5/gs_quant/api/fred/data.py)：返回类型和数据频率处理。
3. [FRED 测试](https://github.com/goldmansachs/gs-quant/blob/8725ddf2ce4b925a7ce68ba90eca353455ac34b5/gs_quant/test/api/test_fred.py)：从 mock 读接口契约，不由 mock 成功推断服务可达。

## 练习（未执行）

先以合成、断网 fixture 检查 provider 返回类型及不规则日期的 last-observation 语义，再画对象/context/provider/result 流程。后续真实 FRED 或 GS 数据使用需单独核对 key、许可、可得时点和 entitlement。

## Our public contribution

[#419](https://github.com/goldmansachs/gs-quant/pull/419) 测试隔离、[#420](https://github.com/goldmansachs/gs-quant/pull/420) FRED/pandas 兼容性均 **OPEN**；它们不是整个 SDK 对所有 pandas 版本兼容的证明。本轮没有新签署贡献协议或重跑上游测试。

## Boundaries

Apache-2.0 代码不提供免费 GS 数据或托管定价权限。此处不处理凭据、不激活服务，也不把官方示例运行成功当作投资收益。

[返回 FICC 路线](README.md) · [Repo 总目录](../README.md)
