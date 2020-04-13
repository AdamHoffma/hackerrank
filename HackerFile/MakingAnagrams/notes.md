An Anagram is a word that is rearranged to form a new word

Given two strings what is the minimum amount of deletions required to make the two strings an anagram

#Returning an integer: Init a counter
#We know they must be the same length so string A - string B is baseline minimum
#What if String A is shorter then String B? Make all integers positive
#How many letters match? Let's play with that
#AFGET AFGCERRR
#The answer will always be how many letters match - that total length of both strings?

#I split the strings and sorted them
#I filtered out the letters that didn't match
#I took the length of letters that matched and subtracted that from string 1 and string 2 and added it together
#Only 3 tests passed
