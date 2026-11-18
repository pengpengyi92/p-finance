# Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment

**Cataloged:** 2026-11-18T23:55:10+08:00 (Asia/Shanghai, UTC+08:00).

- **作者：** Saizhuo Wang、Hang Yuan、Leon Zhou、Lionel Ni、Heung-Yeung Shum、Jian Guo。
- **正式版本：** [ACL Anthology](https://aclanthology.org/2025.emnlp-demos.14/)，EMNLP 2025 **System Demonstrations**，第 196–206 页，DOI [10.18653/v1/2025.emnlp-demos.14](https://doi.org/10.18653/v1/2025.emnlp-demos.14)。
- **预印本：** [arXiv:2308.00016](https://arxiv.org/abs/2308.00016)。引用会议结果优先用正式版本；此条不是 Alpha-GPT 2.0 的单独预印本。

## 收录理由

虽然发表在自然语言处理会议，这篇论文解决的是量化股票投资中的 alpha 因子挖掘：用 LLM 将研究者的自然语言想法转成可检验的因子候选，再由人迭代。论文报告了在 **WorldQuant International Quant Championship** 的评估。竞赛结果是作者报告的证据，不等于实盘收益、可交易性，或对原平台数据/代码的访问权限。

## 一个可讨论的复现实验（NOT_RUN）

固定股票池、特征可用时间和样本外区间，用合成面板或自己有权使用的数据，对比手写因子与相同搜索预算下的 LLM 候选。先测试前视泄漏和未来收益标签对齐，再比较样本外横截面 Rank IC、稳定性与换手；若做组合回测，单列成本与约束。记录随机种子、模型与提示版本、试验次数和失败样例。此建议不复刻竞赛平台，不声称论文结果已被独立验证。

[回到 Academic Papers](README.md) · [分享读书笔记、使用经验或复现结果 #15](https://github.com/pengpengyi92/p-finance/discussions/15)
