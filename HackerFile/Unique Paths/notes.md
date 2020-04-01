If a robot is in an x y grid starting at square 1, 1 and must reach the bottom right square, 
can only move right or down, how many possible paths to the target are there
based on how big the grid is.

To solve this problem we will use recursion where we subtract a path from x and a path from y until we reach one path
and add it all together. I'll draw a diagram of how that would work.

Algorithm:  (x-1, y) + (x, y-1)

We will input x(3) and y(3)

(  2,     3  )              +           (    3,         2)
   /       \                                 /           \
(1, 3)    (2,   2)                         (2,   2)       (3, 1)
          /     \                           /     \          
       (1, 2)   (2, 1)                   (1, 2)   (2, 1) 

We instantiate a base case of x or y equaling 1 to return 1
Now anytime in our tree x or y equals 1 we return a 1 and add them
together. Hence the addition symbol between the to recursive calls.
The addition symbol adds the return statement. 