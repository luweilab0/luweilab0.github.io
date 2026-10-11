---
layout: page
permalink: /team/
title: Team
lang: en
lang_ref: team
nav: true
nav_order: 3
description:
_styles: |
  .post-header { display: none; }
---

<div class="team-card card p-3">
  <div class="team-card-photo">
    {% include figure.liquid loading="eager" path="assets/img/wei-lu.jpg" class="img-fluid z-depth-1 rounded" alt="Dr. Wei Lu" %}
  </div>
  <div class="team-card-info">
    <p class="team-card-name">Dr. Wei Lu <a href="https://smart.org.cn/faculty/luwei" class="cv-link" target="_blank" rel="noopener noreferrer">(SMART faculty page)</a></p>
    <p class="team-card-title">Senior Investigator</p>
    <div class="team-card-contact">
      <span><i class="fa-solid fa-envelope"></i>luwei@smart.org.cn</span>
    </div>
    <p class="team-card-bio">Wei Lu received his PhD at New York University (advisor: Edward Ziff) and completed postdoctoral training in the lab of Roger Nicoll at UCSF. He was a tenured Senior Investigator at NIH/NINDS from 2012 to 2025, and joined SMART full-time in 2025.</p>
    <p class="team-card-bio">Honors: 2019 NIH NINDS Director's Award; 2011 NIH NIMH Principal Investigator Development Award.</p>
  </div>
</div>

<div class="page-section">
  <h2>Team Members</h2>
  <p class="team-card-bio">Our team consists of postdoctoral fellows, graduate students, and research assistants.</p>
  {% for member in site.data.team %}
  <div class="team-card card p-3">
    <div class="team-card-photo-blank"></div>
    <div class="team-card-info">
      <p class="team-card-name">{{ member.label_en }}</p>
      <p class="team-card-bio">{{ member.text_en }}</p>
    </div>
  </div>
  {% endfor %}
</div>

<div class="page-section">
  <h2>Alumni</h2>
  <div class="placeholder">
    <span class="ph-label">Alumni list</span>: Please add lab alumni (name, role while in the lab, current position).
  </div>
</div>
