   
def countSubstrings(string):
    
    counter = len(string)
    lp = 0
    rp = lp + 1
    tempstr = list(string[lp] + string[rp])
    print (len(string)-1) 
    #print(rp + 1)
    print(string[lp])
    print(string[rp])
    print(tempstr)
    while lp < len(string) -1:
        if string[rp] == s[lp]:
            substring(tempstr)
            rp + 1


countSubstrings("abcdes")






