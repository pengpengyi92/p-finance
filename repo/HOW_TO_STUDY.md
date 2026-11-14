# How to Study a Finance Repository

**Updated:** 2026-11-14 (Asia/Shanghai). 给人和 Agent 的同一套证据标准。

## 从一个问题开始

先选你想弄清的问题，再选库：现金流/资本成本去 [公司金融](corporate-finance/README.md)，曲线/定价/风险去 [FICC](ficc/README.md)。目录收录不是推荐购买、生产验收或上游背书。

1. **Source / rights**：记录官方 URL、commit/release、许可、第三方依赖和数据权限。无法确定就暂停复制、安装或运行；尤其先读 rateslib 的边界。
2. **Read**：README → 一个核心函数 → 对应测试 → 最小使用示例。先分清输入、单位、时间、输出和异常。
3. **Question**：提出可证伪问题，例如“对相同现金流与复利口径，两种实现是否得到相同 PV？”
4. **Baseline**：手算/独立小公式；不要拿同一被测函数的输出当真值。
5. **Fixture**：优先固定 synthetic 数据、时钟、随机种子和依赖。标签、市场可得日与执行时点分开。
6. **Experiment**：小范围比较，至少包含一个无效输入/负面对照；不连接真实交易、不自动下载受限数据或调用收费服务。
7. **Report**：保存命令、环境、commit、输入 fingerprint、成功/失败和限制。测量前写 UNMEASURED，没跑写 NOT RUN。
8. **Discuss / contribute**：先查已存在的 Issue/PR，按上游贡献规则交流；任何新 DCO/CLA、付费或数据权限都是单独审批事项。

## 最小学习记录模板

```text
Question:
Official repository / pinned commit:
License / data rights:
Baseline:
Change / comparison:
Fixed fixture / as-of conventions:
Environment / exact command:
Measure: expected vs observed, tolerance, cost
Result: PASS / FAIL / NOT RUN
Trade-off / limitations:
Next Action:
```

把完成的小案例放在 P-Finance 的 [project/](../project/)；经验总结放 [report/](../report/)，讨论放 [Repo Discussions](https://github.com/pengpengyi92/p-finance/discussions/categories/repo)。不要发布私有工作区、日志、策略、账户或未经授权的数据。

## 维护目录

每次新增或更新档案：更新 last reviewed、当前贡献状态与 [source snapshot](source_snapshot.json)；运行 `python -m unittest discover -s tests/repo_guides -v`。该测试只检查目录契约、已抓取路径和链接，不验证金融模型。

[Repo 总目录](README.md)
