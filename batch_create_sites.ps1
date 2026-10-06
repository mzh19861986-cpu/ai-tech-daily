$token = "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"
$baseDir = "C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

$websites = @(
    @{name="ai-coding-tools"; desc="AI Coding Tools - 最佳AI编程工具推荐"; title="AI Coding Tools"; icon="💻"; tagline="最佳AI编程工具推荐，开发者效率翻倍"},
    @{name="ai-art-tools"; desc="AI Art Tools - AI绘画生成工具大全"; title="AI Art Tools"; icon="🎨"; tagline="AI绘画生成工具大全，设计师必备"},
    @{name="ai-writing-tools"; desc="AI Writing Tools - AI写作助手工具推荐"; title="AI Writing Tools"; icon="✍️"; tagline="AI写作助手工具推荐，内容创作效率提升10倍"},
    @{name="ai-video-tools"; desc="AI Video Tools - AI视频生成工具大全"; title="AI Video Tools"; icon="🎬"; tagline="AI视频生成工具大全，短视频创作者必备"},
    @{name="ai-learning-hub"; desc="AI Learning Hub - AI学习教程与资源"; title="AI Learning Hub"; icon="📚"; tagline="AI学习教程与资源，从零开始掌握AI"},
    @{name="ai-startup-cases"; desc="AI Startup Cases - AI创业成功案例"; title="AI Startup Cases"; icon="🚀"; tagline="AI创业成功案例分析，普通人也能用AI赚钱"},
    @{name="ai-monetization"; desc="AI Monetization - AI变现方法大全"; title="AI Monetization"; icon="💰"; tagline="AI变现方法大全，用AI赚被动收入"},
    @{name="ai-news-brief"; desc="AI News Brief - 3分钟AI快讯"; title="AI News Brief"; icon="⚡"; tagline="3分钟读完当天AI圈大事，忙碌人必备"}
)

foreach ($site in $websites) {
    Write-Host "`n=== Creating $($site.name) ==="
    
    # 1. Create repo
    $headers = @{
        "Authorization" = "token $token"
        "Accept" = "application/vnd.github.v3+json"
    }
    $body = @{
        name = $site.name
        description = $site.desc
        private = $false
        has_issues = $true
        has_wiki = $false
    } | ConvertTo-Json
    
    try {
        Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Method Post -Headers $headers -Body $body -ContentType "application/json" | Out-Null
        Write-Host "  ✅ Repo created"
    } catch {
        Write-Host "  ⚠️ Repo may already exist"
    }
    
    # 2. Clone
    $sitePath = Join-Path $baseDir $site.name
    if (Test-Path $sitePath) {
        Remove-Item -Recurse -Force $sitePath
    }
    git clone "https://${token}@github.com/mzh19861986-cpu/$($site.name).git" $sitePath 2>&1 | Out-Null
    Write-Host "  ✅ Cloned"
    
    # 3. Create index.html
    $html = @"
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$($site.title)</title>
    <meta name="description" content="$($site.tagline)">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a1a; background: #fff; line-height: 1.6; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 2rem; }
        nav { padding: 1.5rem 0; border-bottom: 1px solid #eee; margin-bottom: 4rem; }
        nav .container { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.25rem; font-weight: 700; color: #1a1a1a; text-decoration: none; }
        .hero { text-align: center; padding: 6rem 0; }
        .hero h1 { font-size: 3rem; font-weight: 700; margin-bottom: 1.5rem; letter-spacing: -0.02em; }
        .hero p { font-size: 1.25rem; color: #666; max-width: 600px; margin: 0 auto 3rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 4rem 0; }
        .card { padding: 2rem; border: 1px solid #eee; border-radius: 12px; transition: all 0.2s; }
        .card:hover { border-color: #1a1a1a; transform: translateY(-2px); }
        .card h3 { font-size: 1.25rem; margin-bottom: 1rem; }
        .card p { color: #666; }
        footer { padding: 3rem 0; border-top: 1px solid #eee; text-align: center; color: #999; margin-top: 6rem; }
        @media (max-width: 768px) { .hero h1 { font-size: 2rem; } }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">$($site.icon) $($site.title)</a>
            <div>
                <a href="/about" style="color: #666; text-decoration: none;">关于</a>
            </div>
        </div>
    </nav>
    <div class="container">
        <div class="hero">
            <h1>$($site.icon) $($site.title)</h1>
            <p>$($site.tagline)</p>
        </div>
        <div class="grid">
            <div class="card"><h3>🔥 热门推荐</h3><p>最受欢迎的工具和资源</p></div>
            <div class="card"><h3>🆕 最新更新</h3><p>每天自动更新最新内容</p></div>
            <div class="card"><h3>📊 深度测评</h3><p>真实使用体验，不吹不黑</p></div>
        </div>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 $($site.title) - 由 AI 智能集群自动维护更新</p>
        </div>
    </footer>
</body>
</html>
"@
    Set-Content -Path (Join-Path $sitePath "index.html") -Value $html -Encoding UTF8
    Write-Host "  ✅ Index.html created"
    
    # 4. Git commit and push
    cd $sitePath
    git config user.email "mzh19861986@gmail.com"
    git config user.name "mzh19861986-cpu"
    git add .
    git commit -m "feat: initial site" 2>&1 | Out-Null
    git push origin main 2>&1 | Out-Null
    Write-Host "  ✅ Pushed to GitHub"
    
    # 5. Enable Pages
    $pagesBody = @{
        source = @{ branch = "main"; path = "/" }
    } | ConvertTo-Json
    try {
        Invoke-RestMethod -Uri "https://api.github.com/repos/mzh19861986-cpu/$($site.name)/pages" -Method Post -Headers $headers -Body $pagesBody -ContentType "application/json" | Out-Null
        Write-Host "  ✅ GitHub Pages enabled"
    } catch {
        Write-Host "  ⚠️ Pages may already be enabled"
    }
    
    Write-Host "  📍 URL: https://mzh19861986-cpu.github.io/$($site.name)/"
}

Write-Host "`n=== All done! ==="
