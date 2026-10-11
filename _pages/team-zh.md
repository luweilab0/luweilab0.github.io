---
layout: page
permalink: /team-zh/
title: 团队
lang: zh
lang_ref: team
nav: true
nav_order: 3
description:
_styles: |
  .post-header { display: none; }
---

<div class="team-card card p-3">
  <div class="team-card-photo">
    {% include figure.liquid loading="eager" path="assets/img/wei-lu.jpg" class="img-fluid z-depth-1 rounded" alt="陆伟" %}
  </div>
  <div class="team-card-info">
    <p class="team-card-name">陆伟 <a href="https://smart.org.cn/faculty/luwei" class="cv-link" target="_blank" rel="noopener noreferrer">(SMART 主页)</a></p>
    <p class="team-card-title">资深研究员</p>
    <div class="team-card-contact">
      <span><i class="fa-solid fa-envelope"></i>luwei@smart.org.cn</span>
    </div>
    <p class="team-card-bio">陆伟博士于纽约大学获得博士学位（导师：Edward Ziff），随后在加州大学旧金山分校Roger Nicoll实验室从事博士后研究。2012–2025年任美国国立卫生研究院（NIH/NINDS）终身资深研究员，2025年全职加盟深圳医学科学院。</p>
    <p class="team-card-bio">荣誉：2019年NIH NINDS所长奖；2011年NIH NIMH首席研究员发展奖。</p>
  </div>
</div>

<div class="page-section">
  <h2>团队成员</h2>
  <p class="team-card-bio">我们的团队由博士后、研究生和研究助理组成。</p>
  <div class="team-members-grid">
    {% for member in site.data.team %}
    <div class="team-card team-card-member card p-3">
      <div class="team-card-photo-blank"></div>
      <div class="team-card-info">
        <p class="team-card-name">{{ member.label_zh }}</p>
        <p class="team-card-bio">{{ member.text_zh }}</p>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<div class="page-section">
  <h2>往届成员</h2>
  <div class="placeholder">
    <span class="ph-label">往届成员名单</span>：请补充实验室往届成员（姓名、在组期间职位、现去向）。
  </div>
</div>
