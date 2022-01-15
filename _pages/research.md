---
layout: page
permalink: /research/
title: research
description: >
  by category in reversed chronological order. generated by <a href="https://github.com/inukshuk/jekyll-scholar" target="_blank">jekyll-scholar</a>
years_integration: [2021]
years_covid: [2022,2021, 2020]
years_indocc: [2020, 2019, 2018, 2017]
years_hcap: [2019, 2018, 2017]
nav: true
---
***
<div class="publications">
<h1 class="year">Economic Integration</h1>
{% for y in page.years_integration %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}},topic=integration]* %}
{% endfor %}
</div>
***
<div class="publications">
<h1 class="year">Covid-19 and Inequality</h1>
{% for y in page.years_covid %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}},topic=covid]* %}
{% endfor %}
</div>
***
<div class="publications">
<h1 class="year">Inequality across Jobs</h1>
{% for y in page.years_indocc %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}},topic=indocc]* %}
{% endfor %}
</div>
***
<div class="publications">
<h1 class="year">Human Capital and Intergenerational Mobility</h1>
{% for y in page.years_hcap %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}},topic=hcap]* %}
{% endfor %}
</div>
***

