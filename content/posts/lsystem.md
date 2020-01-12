Title: Lindenmayer Systems
Date: 2019
Category: Python
Tags: natural patterns, js, python
Slug: lsystem
featured_image: img/dog2.jpeg
Author: baltasar
Summary: An interactive cellular automata written in javascript 
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
| 3 | 0 |

These strings can in turn be used to represent different systems. The example, for example, can be used to generate the following:


In this case, A means branch to the left, and B means branch to the right. The degree of this turn is a constant, but it doesn't have to be that way. We can introduce constants which 

## Why?
L-systems can be used to model many natural phenomena, such as intricate plants and flowers. They can also be used to generate fractals, such as the Sierpinski triangle. The aim of this project was to make a program that could display all different types of systems. 

## How?
The program was originally written in Python using the Processing[] library, but has been translated to Javascript and P5.JS for the sake of embedding.