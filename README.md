# 网站编辑指南 / Website Editing Guide

本网站由 Jekyll 生成并托管于 GitHub Pages。修改任何文件并提交（commit）后，网站会在约 1 分钟内自动重建上线。
This site is built with Jekyll and hosted on GitHub Pages. Commit any change and the site rebuilds automatically in about a minute.

**无需安装任何软件**：直接在 github.com 网页上打开对应文件，点右上角铅笔图标（Edit）即可编辑，保存时选择 "Commit changes"。
**No software needed**: open the file on github.com, click the pencil icon (Edit), and choose "Commit changes" to save.

## 改什么内容，编哪个文件 / Which file to edit

| 内容 Content | 文件 File |
|---|---|
| 新闻 News | `_data/news.yml` |
| 论文 Publications | `_data/publications.yml` |
| 团队成员 Team members | `_data/team.yml` |
| 首页 / 研究 / 招聘 / 联系等页面文字 | `index.html`、`research.html`、`recruitment.html`、`contact.html` 等对应 `.html` 文件 |
| 页眉、页脚、导航 | `_layouts/default.html`（谨慎修改 / edit with care） |

## 示例 / Examples

添加一篇论文（加在 `_data/publications.yml` 最上方；`Lu W*` 的星号表示通讯作者）：
Add a paper (at the top of `_data/publications.yml`; the `*` in `Lu W*` marks the corresponding author):

```yaml
- year: 2026
  authors: 'Zhang S, Li M, Lu W*'
  title: 'Paper title, with ending period.'
  journal: 'Neuron'
  detail: '100(1), 1-12'
```

添加一条新闻（加在 `_data/news.yml` 最上方；`link_` 开头的三行可选，没有链接就删掉）：
Add a news item (at the top of `_data/news.yml`; the `link_` lines are optional — delete them if there is no link):

```yaml
- date: '2026-10'
  title_zh: '中文标题'
  title_en: 'English headline'
  text_zh: '中文正文。'
  text_en: 'English text.'
  link_url: 'https://example.com/report'
  link_zh: '阅读报道 →'
  link_en: 'Read more →'
```

添加一名团队成员（加在 `_data/team.yml` 中）：
Add a team member (in `_data/team.yml`):

```yaml
- label_zh: '张三'
  label_en: 'San Zhang'
  text_zh: '博士后 — 研究方向：GABA突触可塑性。'
  text_en: 'Postdoc — research focus: GABAergic synaptic plasticity.'
```

## 注意事项 / Notes

- YAML 文件里所有文字都用单引号 `'...'` 括起来；文字内若有撇号（如 `lab's`），写成两个单引号（`lab''s`）。
  In YAML files, wrap all text in single quotes `'...'`; double any apostrophe inside (`lab''s`).
- 页面文字均为中英双语：中文放在 `<span class="lang-zh">…</span>`，英文放在 `<span class="lang-en">…</span>`，两者都要保留。
  All page text is bilingual: keep both `<span class="lang-zh">…</span>` and `<span class="lang-en">…</span>`.
- 编辑 `.html` 页面时，只改 `---` 下方的主体内容；文件顶部的 front matter（`layout`、`title` 等）不要删。
  When editing `.html` pages, only change the content below the `---` front matter block; do not delete the front matter.
- 论文总数、年份分组会自动更新，无需手动修改。/ The paper count and year grouping update automatically.
