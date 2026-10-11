# Lu Lab Website — Plan

**Working name:** Lu Lab (陆伟实验室 / Molecular Cognition Lab, 分子认知实验室)
**PI:** Prof. Wei Lu (陆伟) — Senior Investigator (资深研究员), Deputy Director of the Institute of Neuromodulation and Cognition (INC, 神经调控与认知研究所), SMART (深圳医学科学院 / Shenzhen Medical Academy of Research and Translation), Shenzhen.
**Status:** Mock site built (v1) — all 7 pages done, placeholders in place.

## 6. Next steps

1. Get Prof. Lu's sign-off on this plan (matrix concept, 4th character 调, domain strategy).
2. Register `lulab.org` at Cloudflare (account + ~$11 payment — needs Prof. Lu's or your action).
3. ~~Build the mock static site in this repo with placeholders.~~ **Done (v1 mock):** `index.html` (hero + 聚/散/转/调 matrix + highlights), `research.html`, `team.html`, `publications.html`, `news.html`, `recruitment.html`, `contact.html`; bilingual zh/EN toggle; shared design in `assets/css/style.css`, toggle logic in `assets/js/main.js`. Content needing team input is marked with dashed orange `.placeholder` boxes.

---

## 1. About Prof. Wei Lu (verified facts, for website content)

- Joined SMART full-time May/June 2025, recruited from NIH/NINDS where he was a tenured Senior Investigator (2012–2025).
- PhD: New York University (advisor: Edward Ziff). Postdoc: UCSF (Roger Nicoll lab).
- Lab: 分子认知实验室 (Molecular Cognition Lab), Weiguang Life Science Park, Guangming District, Shenzhen.
- Emails: luwei@smart.org.cn (PI), gaba@smart.org.cn (lab recruitment).
- Research: development and regulation of GABAergic (inhibitory) synapses; GABA-A receptor auxiliary subunits (discovered Shisa7 and TMEM132B); molecular/circuit mechanisms of anxiety, depression, anesthesia, sleep, and alcohol action; goal of next-generation GABA-A-receptor-targeted drugs.
- Three official research directions:
  1. 调控GABA突触发育与传递的分子机制及其在动物行为和神经疾病中的作用
  2. 新型GABAA受体辅助亚基及GABAA受体精神药理学
  3. 麻醉和意识的分子与神经环路机制
- 50+ first/corresponding-author papers in Science, Cell, Neuron, PNAS, Nature Communications, Molecular Psychiatry, Cell Reports, etc.
- Selected papers (from SMART faculty page): Science 2019 (Shisa7/benzodiazepines), Cell 2024 (TMEM132B/alcohol), Neuron 2017 (Neuroligin2/Slitrk3), PNAS 2024 (anxiety), PLOS Biology 2022 (sleep/wake plasticity), Cell Reports 2021 ×2, Neuron 2013, Neuron 2009.
- Honors: 2019 NIH NINDS Director's Award; 2011 NIH NIMH PI Development Award.
- Google Scholar profile exists (email-verified, smart.org.cn); ORCID 0000-0001-6668-8432 (near-verified).
- Sources: smart.org.cn/faculty/luwei, smart.org.cn/en/detail/985.html, sciencenet.cn news 2025-06, 光明网 feature 2025-06-18.

> Important: his work is synaptic neuroscience, NOT phase separation/condensates. The 聚 metaphor = receptor clustering / synapse assembly, which is literally what he studies.

---

## 2. Front page concept — the 2×2 matrix

Four quadrants, each a single Chinese character. **Per user's direction: all four characters map to the lab's scientific directions only — no lab-culture/people mappings.** Each quadrant has a stylized SVG scientific illustration (original artwork, `assets/img/`), to be replaced later with real figures if the team prefers.

| Char | Meaning | Scientific theme (Lu Lab) | Illustration |
|---|---|---|---|
| 聚 jù | assemble | **Synapse assembly** — GABA-A receptors and auxiliary subunits (Shisa7, TMEM132B) clustering into functional inhibitory synapses | synapse with clustered postsynaptic receptors |
| 散 sàn | disperse | **Receptor trafficking** — diffusion, endocytosis, dynamic exchange in/out of synapses; phasic vs. tonic inhibition | receptors dispersing along membrane |
| 转 zhuǎn | transform | **State transitions** — sleep/wake modulation of inhibitory plasticity; anesthesia and consciousness mechanisms | EEG/state-transition motif |
| 调 tiáo | modulate | **Allosteric modulation** — benzodiazepines, alcohol, anesthetics modulating GABA-A receptors; next-gen drug targets | receptor channel with modulator binding |

All four quadrants link to `research.html`. The 调 (tiáo) choice also matches the Institute of Neuromodulation and Cognition's namesake — a bonus, not the rationale.

**Recommended 4th character: 调 (tiáo)** — it completes a verb quartet (assemble → disperse → transform → modulate) that reads as a description of synaptic function, and matches the Institute of Neuromodulation and Cognition.
Alternatives: **通 tōng** (connect — synaptic transmission, bench-to-bedside connection), **合 hé** (combine — collaboration), **生 shēng** (life/growth — training people), **用 yòng** (apply — clinical impact).

Each quadrant should expand/hover into a short line + link into the relevant site section. Final mapping can be adjusted with Prof. Lu — the science layer is real, the content layer is a proposal.

---

## 3. Site structure

Top navigation (standard lab-site format):

- **Research 研究** — the three official directions, with figures (placeholders for now)
- **Team 团队** — PI bio; members grid (photos + roles, to be filled by his team)
- **Publications 论文** — selected list verified above + link to Google Scholar; full list later
- **News 新闻** — e.g., joining SMART (June 2025), Cell 2024 paper coverage
- **Recruitment 招聘** — open positions (lab recruits via gaba@smart.org.cn); link to SMART career page
- **Contact 联系** — address (Weiguang Life Science Park, Guangming, Shenzhen), emails, map

Front page: hero with lab name + one-line mission, then the 聚/散/转/调 2×2 matrix as the visual centerpiece, then brief news/publication highlights, footer with SMART/INC affiliation.

**Bilingual from day one (中文/EN toggle)** — a Shenzhen lab recruiting internationally needs both. Default 中文, EN toggle; keep content files parallel so either language stays in sync.

---

## 4. Domain & hosting (avoiding ICP备案)

Key legal fact: ICP filing is triggered by **server location**, not the domain. Any host outside mainland China (incl. Hong Kong) needs no filing. Avoid `.cn` entirely — CNNIC mandates real-name verification for all `.cn` registrations. Avoid Chinese registrars for any TLD (they require 实名认证 even for `.org`, incl. Alibaba Cloud's international site).

**Decided setup (~US$10–11/year total):**
1. **Domain:** `lulab.org` — confirmed available (checked via RDAP; `lulab.com` and `lu-lab.com` are taken).
2. **Registrar:** Cloudflare Registrar — at-cost pricing (~$10–11/yr, renewal = registration price), free WHOIS privacy, no real-name verification.
3. **Hosting:** Cloudflare Pages (free tier), auto-deploys from GitHub, custom domain bound via Cloudflare DNS (same account, one click). Never rely on the default `*.pages.dev` subdomain from mainland China.
4. **Repo:** GitHub (canonical, account to be created for the lab), with a Gitee mirror for reliable mainland access.

**Fallbacks:**
- Netlify + custom domain — best measured mainland reachability among free tiers (95.6% success in a 137-node probe); can run in parallel and flip DNS.
- Hong Kong VPS (~¥32–55/month, Tencent Lighthouse HK) — best speed/reliability without ICP, near-domestic latency, but more ops work.
- GitHub Pages — free but intermittently slow/blocked in the mainland; acceptable last resort.

**Avoid:** Vercel (blocked in mainland), `.cn` domains, any mainland hosting/CDN (triggers ICP), Chinese registrars.

Residual risk: any overseas-hosted site can be throttled at the GFW's discretion; for a low-traffic academic page the risk is low. Test the final domain from multiple mainland networks before launch (itdog.cn / ping.chinaz.com multi-node probes).

**Also worth asking Prof. Lu:** whether SMART would host a lab page under smart.org.cn infrastructure — that would sidestep the whole issue institutionally.

---

## 5. Technical approach (for the mock phase)

- Static site (no backend needed): plain HTML/CSS/JS or a static generator. Static = trivially hostable on all the options above, easy for the team to hand around.
- Mock phase: build with verified content from §1 and clearly marked placeholders (e.g., `[团队照片待补充]`) wherever his team must supply material.
- Content items to request from his team:
  - PI portrait + lab photos
  - Team member list: names, roles, photos, short bios
  - Full publication list (or confirmation to auto-pull from Google Scholar/ORCID)
  - Recruitment details: open positions, requirements, how to apply
  - Any preferred lab logo / color scheme / Chinese lab name usage
  - Confirmation of the 4th matrix character and quadrant mappings
  - Preferred domain name choice

---

## 6. Next steps

1. Get Prof. Lu's sign-off on the site concept (matrix, 4th character 调).
2. Register `lulab.org` at Cloudflare (account + ~$11 payment — needs Prof. Lu's or your action).
3. ~~Build the mock static site in this repo with placeholders.~~ **Done (v1 mock):** `index.html` (hero + 聚/散/转/调 matrix + highlights), `research.html`, `team.html`, `publications.html`, `news.html`, `recruitment.html`, `contact.html`; bilingual zh/EN toggle; shared design in `assets/css/style.css`, toggle logic in `assets/js/main.js`. Content needing team input is marked with dashed orange `.placeholder` boxes.
4. Iterate with his team filling in real content (photos, members, full publication list, recruitment details).
5. Create lab GitHub account, push repo, deploy to Cloudflare Pages, bind `lulab.org`, test from mainland networks, launch.
