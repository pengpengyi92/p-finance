# P-Finance 行业仓库目录扩展

**2026-11-20（Asia/Shanghai）** · [可展开清单](../repo/market-map.md) ·
[规范来源账本](../repo/finance-topics.json)

## 范围与结果

原目录为 137 个不重复公开仓库、184 个专题位置。此次检索银行、财富管理、
私募股权、创业投资、证券、交易所、基金、保险和金融数据相关工具：

- 63 个候选名称来自 GitHub 主题/关键词检索、官方项目入口及既有目录。
  55 个通过公开身份、提交和 README 核验，其中 2 个已在账本；新增 53 个。
  8 个候选名称未完成规范仓库解析，未计入；不据此判断上游是否存在或开源。
- 为 29 个既有仓库增补具体跨列用途，旧提交、README、许可和原核对时间保留。
  合计 **190 个不重复仓库、302 个专题位置、70 个跨专题仓库**。
- 12 个专题归入 8 个可展开行业组。银行组内对公、投行、FICC、资产托管、
  财富管理合并去重后有 144 个仓库。交易所页面分列撮合、数据服务和数字资产客户端。
  编号为检索顺序，不是质量或收益排名。

这不是全网普查。未取得公开入口、固定 README 和规范提交的候选不入表。
未解析名称：`hledger/hledger`、`hftbacktest/hftbacktest`、
`timpalpant/go-itch`、`lifelib-dev/modelx`、`finnhubio/finnhub-python`、
`gleif-it/gleif-api`、`WindQuant/WindPy`、`qichacha/qcc-openapi`。
后续可从组织主页或项目迁移说明重新核对规范名称。

## 核对办法

从 GitHub 官方 API 核对规范的 owner/name、公开状态、归档/派生状态、
默认分支提交及其根文件树。再从同一固定提交读回 README 与许可文件（若存在）
的 Git blob 标识；没有许可入口、不明确或有额外使用限制的项目标作阅读参考。
代码、规范、第三方数据、商业 API 与账户权利各自独立。

已有节点保留 2026-11-18 的取样；新增节点单独记 `observed_at`、
`readme_blob`、`license_blob`。项目用途是基于公开来源的研究路线，
不是组织部署声明或工具正确性认证。

## 商业数据服务

| 入口 | 在目录中的处理 |
| --- | --- |
| [Bloomberg API Library](https://professional.bloomberg.com/support/api-library/) | 官方 SDK 文档；`underloam/xbbg`、`matthewgilbert/blp` 单列为独立封装，仍须 SDK、账户和数据权限 |
| [Wind 数据接口服务](https://www.wind.com.cn/mobile/WDS/sapi/zh.html) | 官方商业数据服务，仅链接文档，不将未核验公开代码算进仓库数 |
| [企查查开放平台](https://openapi.qcc.com/) | 企业信息的官方商业 API，仅列服务参考；未采集企业记录或个人信息 |

## 离线复查

```sh
python scripts/render_finance_repository_topics.py --check
python -X utf8 -m unittest discover -s tests/repo_guides -v
```

未安装或运行任何新增上游代码、未调用商业接口、未作出投资或承保判断。
应用能力、生产适用性及金融表现均为 **NOT_RUN / UNMEASURED**。
