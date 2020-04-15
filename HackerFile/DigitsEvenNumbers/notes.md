Given an array nums of integers, return how many of them contain an even number of digits.
example: [12, 1, 123, 4356] ans = 12 (12 and 4356)

#It's returning a count so init a counter
#will have to loop through array and count digits 
#Cant count digits of an integer but you can a string
#use toString and get length
#If length % 2 == 0 add 1 to counter