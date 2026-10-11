# 网站编辑指南 / Website Editing Guide

本网站使用 al-folio 主题的 Jekyll 构建，结构与 zhiwen10.github.io 相同，托管于 GitHub Pages。修改任何文件并提交（commit）后，网站会自动重建上线。
This site is built with Jekyll using the al-folio theme (same structure as zhiwen10.github.io) and hosted on GitHub Pages. Commit any change and the site rebuilds automatically.

**无需安装任何软件**：直接在 github.com 网页上打开对应文件，点右上角铅笔图标（Edit）即可编辑，保存时选择 "Commit changes"。
**No software needed**: open the file on github.com, click the pencil icon (Edit), and choose "Commit changes" to save.

## 改什么内容，编哪个文件 / Which file to edit

| 内容 Content | 文件 File |
|---|---|
| 新闻 News | `_news/` — 每条新闻两个文件：英文 `YYYY-MM-DD-名称.md`，中文 `YYYY-MM-DD-名称-zh.md` |
| 论文 Publications | `_bibliography/papers.bib`（BibTeX；每个条目 `@article{...}`） |
| 团队成员 Team members | 占位卡片：`_data/team.yml`；正式成员卡片：`_pages/team.md` 与 `_pages/team-zh.md` |
| 首页 / 研究 / 招聘 / 联系等页面文字 | `_pages/` 下对应的 `.md` 文件，每页分英文（如 `research.md`）和中文（`research-zh.md`）两个文件 |
| 页眉、页脚、导航 | `_includes/header.liquid`、`_includes/footer.liquid`（谨慎修改 / edit with care） |
| 全站设置（标题、邮箱等） | `_config.yml`（谨慎修改 / edit with care） |

## 示例 / Examples

添加一篇论文（加在 `_bibliography/papers.bib` 中；`Lu*` 的星号表示通讯作者，`†` 表示共同第一作者，标在姓后面）：
Add a paper (in `_bibliography/papers.bib`; `*` marks the corresponding author and `†` co-first authors, attached to the last name):

```bibtex
@article{zhang2026paper,
  title={Paper title},
  author={Zhang, S and Li, M and Lu*, W},
  journal={Neuron},
  volume={100},
  number={1},
  pages={1--12},
  year={2026},
}
```

添加一条新闻（在 `_news/` 新建两个文件，文件名以日期开头；`lang: en` 为英文、`lang: zh` 为中文）：
Add a news item (create two files in `_news/`, names starting with the date; `lang: en` for English, `lang: zh` for Chinese):

```markdown
---
layout: post
date: 2026-10-01 09:00:00+0800
inline: true
related_posts: false
lang: en
---

**Headline** — News text. [Optional link →](https://example.com/report)
```

添加一名团队成员（占位卡片在 `_data/team.yml` 中添加；正式成员仿照 `_pages/team.md` 中 PI 卡片的写法，中英文页面各加一份）：
Add a team member (placeholder cards go in `_data/team.yml`; for a full member card, copy the PI card pattern in `_pages/team.md`, once per language):

```yaml
- label_zh: '张三'
  label_en: 'San Zhang'
  text_zh: '博士后 — 研究方向：GABA突触可塑性。'
  text_en: 'Postdoc — research focus: GABAergic synaptic plasticity.'
```

## 注意事项 / Notes

- 中英文是两个独立页面文件：英文 `xxx.md`，中文 `xxx-zh.md`；导航上的 EN/中文 按钮通过 front matter 里的 `lang_ref`（两页相同）自动配对。改动内容时两个文件都要改。
  English and Chinese are separate page files: `xxx.md` (en) and `xxx-zh.md` (zh); the EN/中文 nav button pairs them via the shared `lang_ref` in the front matter. Always update both.
- YAML 文件里所有文字都用单引号 `'...'` 括起来；文字内若有撇号（如 `lab's`），写成两个单引号（`lab''s`）。
  In YAML files, wrap all text in single quotes `'...'`; double any apostrophe inside (`lab''s`).
- 编辑 `.md` 页面时，只改 `---` 下方的主体内容；文件顶部的 front matter（`layout`、`lang`、`lang_ref` 等）不要删。
  When editing `.md` pages, only change the content below the `---` front matter block; do not delete the front matter.
- 论文按年份自动从新到旧分组显示，无需手动修改。/ Papers are grouped by year automatically, newest first.
- 首页聚散转调四象限的插图在 `assets/img/`（`ju.svg`、`san.svg`、`zhuan.svg`、`tiao.svg`）。/ The four quadrant illustrations on the front page live in `assets/img/`.
