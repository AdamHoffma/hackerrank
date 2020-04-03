Karl has an array on integers. He wants to reduce the array until all remianing elements are equal. Determine the minimum number of elements to delete to reach his goal.

For example, if his array is [1, 2, 2, 3] we see that he can delete the 2 elements 1 and 3 leaving [2, 2]. He could also delete both 2s and either the 1 or the 3, that would take 3 deletions. The minimum number of deletion is 2. 

# Wants a count of deletions as return
# The number that appears most often how much it appears - len(array)
# Loop through the array and place the values in a object as the key value is frequency
# If an integer appears more then once increment it's value in object
# Grab max value from the object and subtract from length of array
# return sum