# Strata — 产品、市场数据与风险分层

**Last reviewed:** 2026-11-14 (Asia/Shanghai). [Official repository](https://github.com/tradingtechnologies/Strata) · [Pinned README](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/README.md) · [License](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/LICENSE.txt).

来源提交：`171b1c3c9347e36534f014779064b1ff1bc19216`。只收录公开指引和链接，不镜像源码或市场数据。完整来源与贡献状态见 [source snapshot](../source_snapshot.json)。

## 用途

研究 Java 金融库如何分离产品描述、市场数据、曲线校准、定价和敏感度。适合对照交易台工程设计，而不是只抄一个期权公式。

## 先读

1. [Normal formula](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/modules/pricer/src/main/java/com/opengamma/strata/pricer/impl/option/NormalFormulaRepository.java)：Bachelier 模型及隐含波动率边界。
2. [Black formula](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/modules/pricer/src/main/java/com/opengamma/strata/pricer/impl/option/BlackFormulaRepository.java)：零波动率/到期极限。
3. [Smith-Wilson 曲线函数](https://github.com/tradingtechnologies/Strata/blob/171b1c3c9347e36534f014779064b1ff1bc19216/modules/math/src/main/java/com/opengamma/strata/math/impl/interpolation/SmithWilsonCurveFunction.java)：曲线外推与数值稳定性。

## 练习（未执行）

固定合成 forward/strike，比较 normal 与 lognormal 报价及其单位；再检查零波动率和极端参数。不要把 stress-case 失败夸大成常规市场校准失效，也不要把 normal vol 与 Black vol 直接相加。

## Our public contribution

[#2825](https://github.com/tradingtechnologies/Strata/pull/2825) 和 [#2826](https://github.com/tradingtechnologies/Strata/pull/2826) 均 **OPEN**；原始问题/候选修复归属以 PR 对外部报告者的致谢为准。另有 Smith-Wilson [Issue #2828](https://github.com/tradingtechnologies/Strata/issues/2828)，**OPEN**。本次未重跑 Java 套件或核定 CI 成功。

## Boundaries

Apache-2.0。正式上游现为 tradingtechnologies/Strata，旧 OpenGamma 路径可能重定向。需按上游要求准备 Java/Maven；此处没有构建、部署或执行交易。

[返回 FICC 路线](README.md) · [Repo 总目录](../README.md)
