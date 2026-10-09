# 📚 Dev.to 热门技术文章 - 2026-10-08

> 从 Dev.to 社区精选的高质量技术文章 | AI 帮你提炼精华 | 共 5 篇

## 1. [Publishing Threads Carousels from Worker-Hosted Images](https://dev.to/raylabs/publishing-threads-carousels-from-worker-hosted-images-19ah)

**✨ 精华总结：** 通过Threads API发布多图轮播时，每个图片项都必须有一个可公开访问的URL，传统做法是先上传到S3或R2这类对象存储再调API。这篇文章的价值在于：它给出了一种在纯serverless worker环境里直接托管图片、省掉独立存储层的方案，特别适合不想为了发几张图就额外维护一套存储基础设施的开发者。

## 2. [I break into apps for a living. AI just made my job easier.](https://dev.to/kstriabintang/i-break-into-apps-for-a-living-ai-just-made-my-job-easier-2akk)

**✨ 精华总结：** 一位从渗透测试转做 AI 全栈工程师的安全研究员发现，现在入侵应用比以前更容易了。原因不是防守方变懒，而是大家开始大量交付自己从未读过的代码——AI 生成的代码让「没人真正理解系统」成了常态，攻击面随之扩大。

## 3. [Python Session Revocation — What Actually Matters in Concrete Forgot-Password Audits](https://dev.to/valenciamoss6824/python-session-revocation-what-actually-matters-in-concrete-forgot-password-audits-35d7)

**✨ 精华总结：** 这篇讲的是忘记密码流程的安全审计要点：核心原则是服务端必须保留会话记录，一旦密码重置改变了账户安全状态就立即吊销旧会话，同时只保存精简的审计投影而非全部请求响应体。关键在于区分"过期"和"吊销"——过期管的是"登录能活多久"，吊销管的是"这个登录现在还算数吗"，而事件响应真正需要的是后者。

## 4. [I built a copy-paste JSON viewer for shadcn/ui](https://dev.to/mnove/i-built-a-copy-paste-json-viewer-for-shadcnui-1k15)

**✨ 精华总结：** 有人做了个 shadcn/ui 版 JSON 查看器组件，直接复制粘贴就能用，解决了 `<pre>{JSON.stringify(data, null, 2)}</pre>` 可读性差、又不想引入带自己样式系统的大型 JSON 库的痛点。如果你在用 shadcn/ui 搭后台或调试面板，这个组件能保持视觉统一，省得自己调样式。

## 5. [MikroTrick: How Two RouterOS Flaws Let Attackers Take Over MikroTik Routers Without a Password](https://dev.to/kozhevniko/mikrotrick-how-two-routeros-flaws-let-attackers-take-over-mikrotik-routers-without-a-password-3nan)

**✨ 精华总结：** MikroTik RouterOS 被曝出六个漏洞，其中两个可组合成名为 MikroTrick 的攻击链，只要设备的 SSH 服务暴露在公网上，攻击者无需密码就能完全接管路由器。CERT Polska 已确认这些漏洞正在被实际利用，CISA 也已将其纳入已知被利用漏洞目录——如果你有 MikroTik 设备，现在就该检查 SSH 是否对外开放并尽快打补丁。

---
*读完有收获？点个赞支持一下原作者~*