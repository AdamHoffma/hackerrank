The goal of this exercise is to take an array of integers and rotate them to the left. 
As an example:
[1, 2, 3, 4]  rotated left two spots becomes
[3, 4, 1, 2]

first approach would be to use push() and feed it the value of shift()
like thusly:  array.push(array.shift())
You see shift() takes the item off the front of the array and shifts everything else left
while push() take an item and puts in the back of the array. So we are pushing the first number in the 
array to the back. 
Use a while loop to do this. Init a counter and say while counter is less then the amount of shifts you want

