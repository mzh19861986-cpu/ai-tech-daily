# 💡 每日开发技巧 - 2026-10-07

> 每天学一个实用技巧，效率慢慢提上来 | 共 3 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文把中国哲学智慧（比如儒家的"中庸"、道家的"无为"）引入了自动驾驶的决策系统，让大语言模型在做驾驶判断时不再只算数值最优，而是学会权衡安全、效率和社会规范之间的微妙平衡。它值得关注，因为这是第一次系统性地把东方哲学框架嵌入自动驾驶决策，可能为"机器如何做出有温度、有分寸的判断"提供一条新思路。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**Why Every SaaS Wants Your Phone Number (and How to Decide When to Give It)**

✨ SaaS 产品要你手机号，核心原因有三个：短信验证比邮箱更防批量注册、手机号是跨平台的稳定身份标识、以及它是触达用户最直接的营销通道。但问题在于，很多产品拿到号码后的用途远超「验证身份」——包括二次营销、数据关联、甚至转手给第三方。这篇文章的价值在于教你区分「真需要」和「假需要」：涉及资金和账户安全的场景可以给，纯营销目的的注册流程能跳就跳。

📎 [阅读原文](https://dev.to/ghostsms/why-every-saas-wants-your-phone-number-and-how-to-decide-when-to-give-it-4pn0)

## 技巧 3

**How to Build a Rotation-Safe Webhook Receiver: Verify Raw Signatures for Property Billing**

✨ 这篇文章讲的是如何搭一个能扛住密钥轮换的 Webhook 接收器——核心做法是：用原始请求体（raw body）验签，而不是解析后的 JSON，否则密钥一换签名就对不上。验签通过后要把密钥绑定到具体的房产账户，把验证证据先落盘入队，等持久化写入成功才返回 200，避免"确认了但没存住"的丢事件问题。

值得关注的点在于它顺带暴露了一个真实故障场景：凌晨 3:07 监控报 webhook_auth_failures_high，住户端 API 还在正常服务，但多个楼栋的支付和维修事件已经被静默拒收了——典型的"表面健康、局部失血"，正是密钥轮换没处理好会踩的坑。

📎 [阅读原文](https://dev.to/quentinbarrett5281/how-to-build-a-rotation-safe-webhook-receiver-verify-raw-signatures-for-property-billing-51kf)

---
*每天一个小技巧，一年就是 365 个进步~*