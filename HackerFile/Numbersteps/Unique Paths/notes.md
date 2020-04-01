If a robot is in an x y grid starting at square 1, 1 and must reach the bottom right square, 
can only move right or down, how many possible paths to the target are there
based on how big the grid is.

To solve this problem we will use recursion where we subtract a path from x and a path from y until we reach one path
and add it all together. I'll draw a diagram of how that would work.

Algorithm:  (x-1, y) + (x, y-1)



