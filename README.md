# Lu Lab Website — One-Page Handover Guide / 网站使用一页指南

**What this is / 这是什么**
The lab website **https://luweilab.com**, built with Jekyll (al-folio theme).
Source code lives in the GitHub repo **github.com/luweilab0/luweilab0.github.io**.
Every change pushed to the `main` branch auto-rebuilds the live site in ~4 minutes.
本网站是实验室官网，源码在 GitHub 仓库中。任何修改推送到 main 分支后约 4 分钟自动上线。

**Accounts / 账号（均基于实验室 Google 账号注册）**

| Account 账号 | What it holds 用途 | Where 地址 |
|---|---|---|
| Google | base account, receives all recovery emails 基础邮箱 | gmail.com |
| GitHub (luweilab0) | the website code + hosting 网站源码与托管 | github.com |
| Cloudflare | the luweilab.com domain (~$11/yr renewal) 域名与DNS | cloudflare.com |

Keep these three logins with the designated lab member. 账号由指定成员保管。

---

## Method 1 — Edit directly on GitHub (no software, 5 minutes) / 方法一：网页直接改

1. Sign in to github.com as **luweilab0**.
2. Open the repo, find the file to edit (see table below), click the **pencil icon ✎**, edit, then **Commit changes**.
3. Wait ~4 minutes, refresh https://luweilab.com.

| To change 想改什么 | Edit this file 编辑哪个文件 |
|---|---|
| Add a news item 加新闻 | create a file in `_news/` (copy an existing one; en + zh pair) |
| Team members 团队成员 | `_data/team.yml` |
| Publications 论文 | `_bibliography/papers.bib` (add `doi={...}` to auto-link) |
| Page text 页面文字 | `_pages/*.md` (each page has en + zh versions) |
| Front-page matrix 首页四格 | `_pages/home.md` / `home-zh.md` |

**Golden rule / 重要原则:** if you are not sure, don't touch `_config.yml`, `_layouts/`, `_includes/`, `_sass/`, `.github/`. 不确定就不要动这些文件。

## Method 2 — Ask an AI agent / 方法二：让 AI 助手改

On a computer with the AI coding tool (e.g., Kimi Code CLI):

```
git clone https://github.com/luweilab0/luweilab0.github.io.git
```

Then just describe the change in plain language, e.g.:
> "Add a news item: our paper was accepted at Neuron on 2026-10-01" / "把张三加到团队成员，博士后"

The agent will edit, preview locally (`bundle exec jekyll serve`), and push. First push asks you to sign in via browser once — after that it's automatic.
AI 会修改、本地预览并推送；首次推送需在浏览器登录一次 GitHub 账号。

---

**If something breaks / 出问题怎么办:** repo → Actions tab shows the build log; the previous version is always recoverable via git history (`git log` / GitHub History button). Domain and hosting emails go to the Google account — watch for the yearly Cloudflare renewal notice.
