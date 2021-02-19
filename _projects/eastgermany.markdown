---
layout: page
title: "German Reunification"
description: What happened in East Germany after reunification?
img: /assets/img/berlin_vir_small.jpg
importance: 1
---

[Wolfgang Dauth](https://sites.google.com/site/dauthecon/), [Sebastian Findeisen](https://sebastian-findeisen.com/), [Tommaso Porzio](https://sites.google.com/view/tommaso-porzio/home) and I have been cranking out German social security records to understand the transforation of the East German labor market. Despite two decades of stagnation, wage growth in the first few years after reunification was spectacular:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/gdp.png' | relative_url }}" alt="" title="German GDP"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/wage.png' | relative_url }}" alt="" title="German Wages"/>
    </div>
</div>
<div class="caption">
    Left: East/West GDP before and after reunification (by location). Right: Average wages (by origin). East in black.
</div>

<hr>

The popular conception is that East Germans gained mostly from migrating West, but the patterns are clear that most of the growth came from ***within*** East (robust to painstaking checks). 

We posit a lot of this growth, in fact, came from workers switching jobs...

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/flows.png' | relative_url }}" alt="" title="between-firm Job Switches"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/oflows.png' | relative_url }}" alt="" title="within-firm Occupational Switches"/>
    </div>
</div>
<div class="caption">
    Left: Share of workers who switch firms. Right: Occupational switches among those who don't switch firms. East in black.
</div>
and extensive and intensive firm restructuring:
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/jobrealloc.png' | relative_url }}" alt="" title="Job Reallocation"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/exwrealloc.png' | relative_url }}" alt="" title="Excess Worker Reallocation"/>
    </div>
</div>
<div class="caption">
    Left: Job Creation and Destruction. Right: Share of swapped workers without changing firm size. East in black.
</div>

## The Cohort-Reallocation Gradient

## Firms before and after Reunification

<hr>
## What else do we do?
It would be nice to show that the reallocation patterns led to causal effects. We do a lot of extra empirical stuff that backs this up, but after all it is impossible to relate average wage growth *over time* to reallocation patterns across worker and firm cohorts *at a given moment in time*---moreover, wage growth would stem from both the worker- and firm-sides, so we need a framework to incorporate them simultaneously. 

Which led us to build a beautiful model of multi-worker firms with hetergeoenous worker matches, endogenous firing and on-the-job search by workers who age over their life-cycle.

### Results coming soon!

<!--
Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/1.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/3.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/5.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/5.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, *bled* for your project, and then... you reveal it's glory in the next row of images.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/6.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/11.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>


The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/" target="_blank">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:
-->