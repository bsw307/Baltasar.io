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

Lindenmayer systems (l-systems), are iterations of strings generated through defined rules. An example could lookas follows:

Constants = *A, B*

Rules = (**A->AB**),(**B->BB**)

Initial string = A

We then repeatedly apply these rules to the string, transforming it.

|Iteration|   |
|---|---|---|---|
| 0 | A |
| 1 | AB |
| 2 | ABBB |
| 3 | ABBBBB |

These strings can in turn be used to represent different systems. The example, for example, was Lindenmayer's model of algae growth.

In this case, A means branch to the left, and B means branch to the right.

## Why?
L-systems can be used to model many natural phenomena, such as intricate biological systems. They can also be used to generate fractals, such as the Sierpinski triangle. The aim of this project was to make a program that could display all different types of systems.

## How?
The program was originally written in Python using the Processing library, but has been translated to Javascript and P5.JS for the sake of embedding it on this site.

## Results
<p style="text-align:center">	
<iframe style="width:400px; height: 500px; overflow: hidden;"  scrolling="no" frameborder="0" src="https://editor.p5js.org/baltasaur/embed/Ojb2DqkV"></iframe> 
</p>