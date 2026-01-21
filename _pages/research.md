---
layout: page
title: research
permalink: /research/
nav: true
---

## published papers
<div class="publications">
{% bibliography --query @*[status=published] %}
</div>

## other work
<div class="publications">
{% bibliography --query @*[status=other] %}
</div>

## working papers
<div class="publications">
{% bibliography --query @*[status=working] %}
</div>
