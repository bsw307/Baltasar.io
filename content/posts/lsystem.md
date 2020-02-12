Title: Lindenmayer Systems
Date: 2019
Category: Python
Tags: natural patterns, js, python
Slug: lsystem
featured_image: img/plant.png
Author: baltasar
Summary: Various interactive lsystems for p5
p5link: https://editor.p5js.org/baltasaur/embed/LU5R2vEzw

# Drawing lindenmayer systems

## What?

Lindenmayer systems (l-systems), are rewriting systems predicated on defined rules. A simple example could look as follows:

> Constants = *A, B*
> 
> Rules = (**A->AB**),(**B->BB**)
> 
> Starting string = A

We then repeatedly apply these rules to the string, transforming it.

Iterations

>1: A
>
>2: AB
>
>3: ABA
>
>4: ABAABABA
>
>5: ABAABABAABAAB

These, seemingly, simple string can in turn be used to model a variety of systems. The example above, for instance, was used by the eponymous Lindenmayer's to model the growth of algae growth patterns. Interestingly enough, the number of letters in each iteration's string corresponds to the Fibonacci sequence.

To make things more interesting, we can add in more rules and symbols. To model more complex structures, such as plants, we also introduce the use of symbols which correspond to drawing angles.

At the bottom of this page, three models are available to try out.

**System 1: Fractal binary tree**

This system has four symbols: **1, 0, [, ]**

The 1 and 0 both correspond to drawing a line, while [ corresponds to saving the location and turning 45° to the left, and ] to jumping back and turning to the right.

The rules are as follow:

> 1 -> 11
>
>0 -> 1[0]0

**System 2: Dragon curve**

This system has four symbols: **X,Y,F,+,-**

F corresponds to drawing a line, + corresponds to turning 90° to the left, and - to turning to the right. X and Y serve no purpose in drawing the figure, only in creating the strings.

The rules are as follow:

> X -> X+YF+
>
>Y -> −FX−Y

**System 3: Fern**

This system has four symbols: **X,F,+,-,[,]**

A combination of the previous systems, F corresponds to drawing a line, while + corresponds to turning 25° to the left, and - to turning to the right. [ and ] correspond to saving and returning to a location, respectively. X serves no purpose in drawing the system, only in creating the strings.

The rules are as follow:

> X -> F+[[X]-X]-F[-FX]+X
>
>F -> FF

## Why?
L-systems can be used to model many natural phenomena, such as plants and bacteria. They can also be used to generate mathematical fractals, such as the Sierpinski triangle. The aim of this project was to make a program that could display all different types of systems.

## How?
The program was originally written in Python using the Processing library, but has been translated to Javascript and P5.JS for the sake of embedding it on this site.

## Results
Click repeatedly on any button to see the development of three types of systems.
<p style="text-align:center">	
<iframe style="width:400px; height: 500px; overflow: hidden;"  scrolling="no" frameborder="0" src="https://editor.p5js.org/baltasaur/embed/Ojb2DqkV"></iframe> 
</p>