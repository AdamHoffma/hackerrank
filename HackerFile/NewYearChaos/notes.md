You have a line. Its an array of integers. 1 through x
An integer can move forward, but it can only move forward at most twice
Figure out how many times a number moved based on array given
[1, 2, 3, 4, 5] becoming [1, 3, 2, 4, 5] denotes 3 moved once  [1, 3, 5, 2, 4]  [2, 1, 3, 4, 5]  [3, 2, 1, 4, 5] [3, 4, 2, 1, 5]
one move
If a number moved more then two spots return TOO CHAOTIC

#Math?
#Let's see.... if 5 moves to position 2... nah that wont work.
#We need to see if any number moved left more then two spots
#And also count the amount of moves.
#We could track number vs index?  5 would have index 4 if it's index is more then 4 -2 TOO CHAOTIC
#Number - 1 - index equals moves?
#What to do with negative numbers? I.E. an integer that has moved back in the queue? 

3 - 1 - 0 = 2
4 - 1 - 1 = 2
2 - 1 - 2 = -1
1 - 1 - 3 = -3
5 - 1 - 4 = 0

