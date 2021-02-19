---
layout: page
title: "German Reunification"
description: What happened in East Germany after reunification?
img: /assets/img/berlin_vir_small.jpg
importance: 1
---

[Wolfgang Dauth](https://sites.google.com/site/dauthecon/), [Sebastian Findeisen](https://sebastian-findeisen.com/), [Tommaso Porzio](https://sites.google.com/view/tommaso-porzio/home) and I have been cranking out German social security records to understand the transformation of the East German labor market. Despite two decades of stagnation, wage growth in the first few years after reunification was spectacular:

<div class="row">
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/wage1992.png' | relative_url }}" alt="" title="German Wages 1992" />
        <figcaption class="figure-caption text-center">1992</figcaption>
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/wage1995.png' | relative_url }}" alt="" title="German Wages 1995"/>
        <figcaption class="figure-caption text-center">1995</figcaption>
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/wage2000.png' | relative_url }}" alt="" title="German Wages 2000"/>
        <figcaption class="figure-caption text-center">2000</figcaption>
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/wage2013.png' | relative_url }}" alt="" title="German Wages 2013"/>
        <figcaption class="figure-caption text-center">2013</figcaption>
    </div>
</div>
<div class="caption">
    Average wages in Germany. White is average, blue is less, red is more.
</div>

The popular conception is that East Germans gained mostly from migrating West, but the patterns are clear that most of the growth came from **within** East (robust to painstaking checks). Another widespread conception is that East Germany was supposed to continue to grow to West German levels (they went from less than half to about two thirds in 5 years, then got stuck there), so the last two decades of stagnation mean something is going wrong.

But maybe slow growth is the natural outcome. Then the question becomes, why did wages grow so rapidly in the beginning?

<hr>

We posit that, in a setting where West institutions were almost perfectly superimposed on the East, labor market adjustment seemed to have followed immediately---despite other fundamental differences that may exist between East and West German workers and firms (which is probably why they stopped growing). 

How did we come to this conclusion? Well, the first few years post-reunification also involved a lot of workers switching jobs...

<div class="row">
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/move1992.png' | relative_url }}" alt="" title="Job-to-Job Switches 1992"/>
        <figcaption class="figure-caption text-center">1992</figcaption>
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/move1995.png' | relative_url }}" alt="" title="Job-to-Job Switches 1995"/>
        <figcaption class="figure-caption text-center">1995</figcaption>
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/move2000.png' | relative_url }}" alt="" title="Job-to-Job Switches 2000"/>
        <figcaption class="figure-caption text-center">2000</figcaption>
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/move2013.png' | relative_url }}" alt="" title="Job-to-Job Switches 2013"/>
        <figcaption class="figure-caption text-center">2013</figcaption>
    </div>
</div>
<div class="caption">
    Between-firm job switches in Germany. White is average, blue is less, red is more.
</div>

and lots of firm restructuring, both *extensive* (change in size) and *intensive* (change in workforce):

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

Job reallocation in year $$t$$ is defined as

$$
    JR_t = \frac{
    \sum_{j\in\mathcal I}|N_{j,t+1}-N_{j,t}|
     + \sum_{j\in\mathcal{N}_{t+1}}N_{j,t+1}
     + \sum_{j\in\mathcal{N}_t}N_{j,t}
     }
    {\sum_j\left(N_{j,t}+N_{j,t+1}\right)}, 
$$

where $$N_j$$ is the employment size of firm $$j$$, $$\mathcal{I}$$ is the set of incumbent firms (that are in existence in both $$t$$ and $$t+1$$), and $$\mathcal{N}_t$$ the set of firms in existence only in year $$t$$.

So job reallocation captures the following. Among all job switches in the economy from one period to the next, how many involved a change in firm size, or firm entry or exit? Then we can also define **excess worker reallocation** as

$$
    EWR_t = \frac{
    H_t + F_t - JR_t\cdot\sum_j\left(N_{j,t}+N_{j,t+1}\right)
     }
    {\min\{N_{j,t},N_{j,t+1}\}}.
$$

where $$H_t$$ and $$F_t$$ are the total number of hires and fires, respectively. Think of it like this. Among all hires and fires in the economy, how many workers were swapped without involving a change in firm size?

<hr>

You might say, those are just time series, and wage growth and reallocation are spuriously correlated. Or, higher productivity injected from the West just incentivized firms and workers to reallocate more.

We want to show that reallocation was an outcome of institutional transformation, and must surely have contributed to wage growth. 

<hr>

## The Cohort-Reallocation Gradient

Take yourself back to 1990 and imagine who would want to switch jobs---the old man who worked in a communist factory for decades, or the 20 year-old who just started a new career in a new Germany? The answer is clear in the data:

<div class="row">
    <div class="col-sm mt mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/wcohorts.png' | relative_url }}" alt="" title="Job-to-Job Switches by Cohort"/>
    </div>
</div>
<div class="caption">
    Between-firm job switches by cohort. East in black.
</div>

In just 5 years, East Germans who started their careers after reunification don't switch jobs any more than their West German counterparts. More surprisingly, East Germans who started their careers before reunification are still switching jobs relatively more often.

## Firms before and after Reunification

By the same token, it was old firms that did most of the restructuring, and still are. Surprisingly, new East and West firms that entered after reunification look almost the same from the get-go!

<div class="row">
    <div class="col-sm mt mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/germany/fcohorts.png' | relative_url }}" alt="" title="Firm Restructuring by Cohort"/>
    </div>
</div>
<div class="caption">
    Firm reallocations over time, by cohort. East in black.
</div>

<hr>

## What else do we do?
It would be nice to show that the reallocation patterns caused wage growth. We do a lot of extra empirical stuff that backs this up, but after all it is impossible to relate average wage growth *over time* to reallocation patterns across worker and firm cohorts *at a given moment in time*---moreover, wage growth would stem from both the worker- and firm-sides, so we need a framework to incorporate them simultaneously. 

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