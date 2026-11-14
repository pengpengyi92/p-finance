# Tencent FiT cross-border payments: FX and settlement work log

**Timestamp:** `2026-11-14T15:18:55+08:00` (Asia/Shanghai). **Evidence:** Public sources and offline examples only.

[Tencent FiT](https://www.fitgroup.com/home) and [TenPay Global](https://www.tencent.com/products/tenpay-global/) provide the public product context. The upstream contributions below went to the official [WeChat Pay Global Skills repository](https://github.com/wechatpay-apiv3/wechatpay-global-skills); we did not verify a separate open TenPay Global FX-team repository.

PPRT is a private internal research repository exploring Tencent CDG, FiT, and FX. This work log mentions that research direction only. It does not reproduce internal material, link to PPRT, or imply any affiliation with Tencent.

## Upstream work

- The earlier [Global Skills #6](https://github.com/wechatpay-apiv3/wechatpay-global-skills/pull/6) and [WeChat Pay Skills #47](https://github.com/wechatpay-apiv3/wechatpay-skills/pull/47) were open at review: no posted reviews, comments, or public PR checks. No changes were needed in response to feedback.
- [Global Skills #7](https://github.com/wechatpay-apiv3/wechatpay-global-skills/pull/7) corrects callback guidance: the price currency, payer currency, and settlement currency can differ. The official worked example is 100 PHP priced, 12 CNY paid, and 2 USD settled. Treating PHP or CNY as the settlement currency gives the wrong ledger classification.
- [Global Skills #8](https://github.com/wechatpay-apiv3/wechatpay-global-skills/pull/8) adds a reconciliation check. In a synthetic statement with payments of 100.00 USD and 80.00 HKD and a refund of 10.00 USD, excluding fees, the two subtotals are 90.00 USD and 80.00 HKD. The arithmetic sum is not a valid currency total.

The references are the [payment-notification field dictionary](https://pay.wechatpay.cn/doc/global/v3/en/4012356834) and [multi-currency pricing and settlement specification](https://pay.wechatpay.cn/doc/global/v3/en/4041899517). Both changes were checked against those public sources and offline examples. No payment endpoint, credentials, or live statement data were used. See [P-Curve's note on why these rates are not market curve inputs](https://github.com/pengpengyi92/p-curve/blob/main/update/2026-11-14-cross-border-fx-settlement-vs-curves.md).

## Validation update — `2026-11-14T15:36:56+08:00` (Asia/Shanghai)

[Skills #47](https://github.com/wechatpay-apiv3/wechatpay-skills/pull/47) independently reproduced a Windows PowerShell 5.1 parse failure: the UTF-8 script contained Chinese text but no BOM. The existing PR was updated in commit `15fa471`. The same three synthetic P12 fixtures (plain path, brackets in directory, brackets in filename) all produced verifiable RSA signatures on Windows PowerShell 5.1.26100.9818 and PowerShell 7.6.9. This is local validation, not upstream CI or merge. No payment endpoint or real certificate was used.
