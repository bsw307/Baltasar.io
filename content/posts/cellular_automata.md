Title: Cellular automata
Date: 2019
Category: Python
Tags: fun with fungi, js, python
Slug: automata
featured_image: img/cell.png
Author: baltasar
Summary: An interactive cellular automata written in javascript 
p5link: https://editor.p5js.org/baltasaur/embed/LU5R2vEzw

# Generalized cellular automata in two dimensions

## What?

This project grew out of my fascination with Conway's "Game of life", which is a particular implementation of a cellular automaton(*CA*). The model consists of a grid of cells, each of which can be in one of two states: dead or alive, represented by 0 and 1, respectively. Rules are then applied to see which cells will be dead and which will be alive in the next frame. In the case of the "Game of life", [four rules](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules) are used.<sup>1</sup>  

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules can be condensed to **B3/S23**, meaning dead cells with **3** neighbours are born, and living cells with **2** or **3** neighbours survive. All other cells die.  


## Why?
Cellular automata exhibit many interesting properties, and are studied as discrete systems. Much attention is given to the evolution of specific patterns, and the classification of different *CA* based on these patterns.

In the model below, three types of patterns can be observed.

1. **Stills** - Patterns that don't change by themselves.

2. **Oscillators** - Changing patterns that return to the same shape given enough iterations.  

3. **Spaceships** - Oscillating patterns which traverse the cell space.

## How?
The program below is written in javascript using the P5.JS library, which enables drawing the cells as well as embedding the file on this page.

## Results
<p style="text-align:center">	
<iframe style="width:400px; height: 500px; overflow: hidden;"  scrolling="no" frameborder="0" src="https://editor.p5js.org/baltasaur/embed/LU5R2vEzw"></iframe> 
</p>

<!-- ## Sources
<sup>1</sup> [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) -->
