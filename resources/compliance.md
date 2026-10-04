# 合规红线清单

> ⚠️ 本文件是硬约束。任何 Agent 任务上线前必须对照本文件逐条检查。

## 一、GitHub 平台禁止项

来源：[GitHub Additional Products Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features)

- ❌ **加密货币挖矿** — 任何形式
- ❌ **未经授权访问**任何服务/设备/数据/账号/网络
- ❌ **将 GitHub Actions 作为商业服务转售** — 不能把 Actions 当云服务器卖给别人用
- ❌ **GitHub Pages 用于商业电商 / SaaS** — Pages 只能做项目文档/个人博客
- ❌ **账户主要内容是广告/推广** — 仓库、Issue、README 不能变成广告板

## 二、爬虫合规

- ✅ 只抓 **公开可访问** 且 **不违反 robots.txt** 的数据
- ✅ 控制频率（尊重 `Retry-After`、每秒不超过 1-2 次请求）
- ✅ 加合理的 `User-Agent`，说明是谁在抓
- ❌ 绕过登录墙、付费墙、验证码
- ❌ 抓取个人隐私数据（PII）
- ❌ 抓取后原样转载受版权保护的内容（可以摘要、引用，但不能全文复制）
- ❌ 大规模并发导致目标站宕机（拒绝服务风险）

## 三、平台 ToS 红线

| 平台 | 禁止自动化行为 |
|------|----------------|
| Reddit | 自动发帖/评论需严格遵守 API ToS，不能用于垃圾内容 |
| YouTube | 自动上传视频需遵守 API ToS，频道必须是自己的 |
| X (Twitter) | 自动化发文限制严格，批量操作会封号 |
| Instagram / TikTok | 第三方自动化几乎都违反 ToS |
| Amazon Associates | 禁止虚假流量、cookie  stuffing |
| Upwork / Fiverr | 禁止 bots 自动投标 |

## 四、支付 / 税务

- ⚠️ 所有收入需依法申报纳税
- ⚠️ Stripe / PayPal 账户必须是自己实名的，不能用 Agent 自动注册新账号
- ⚠️ AdSense 需通过人工审核，不能自动化"养号"
- ❌ 多账号套现、洗钱、虚假交易

## 五、AI 内容合规

- ⚠️ AI 生成内容需标注（部分平台要求）
- ❌ 不能用 AI 生成虚假新闻、深度伪造、诽谤内容
- ❌ 不能抄袭他人原创内容后 AI 改写发布（版权风险）
- ⚠️ 用 AI 生成代码时注意许可证传染性

## 六、安全

- ❌ 不能让 Agent 自动输入密码、支付信息、密钥
- ❌ 不能把 API key / 支付密钥硬编码在公开仓库
- ✅ 所有密钥走 GitHub Secrets
- ✅ 定期审计 Agent 的操作日志

---

## 快速检查清单（每次上线前过一遍）

- [ ] 这个任务会违反 GitHub ToS 吗？
- [ ] 抓取的网站允许爬吗？robots.txt 看了吗？
- [ ] 频率会不会把对方服务器打挂？
- [ ] 内容是原创/摘要，还是直接复制？
- [ ] 支付/账号是我本人实名的吗？
- [ ] 密钥存对地方了吗？
- [ ] 出了问题能一键停掉吗？
