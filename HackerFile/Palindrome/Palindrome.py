
def countSubstrings(string):        
    lp = 0
    rp = lp + 1
    tempstr = list(string[lp] + string[rp])   
    print(len(tempstr)) 
    while lp < len(string) -1:
        if string[rp] == string[lp]:
            substring(tempstr, string)
            rp + 1
        elif string[rp] != string[lp]:
            rp + 1
            tempstr.append(string[rp])
        elif rp == len(string):
            lp + 1
            rp = lp + 1
            tempstr = list(string[lp] + string[rp])

def substring(tempstr, string):
    counter = len(string)
    if len(tempstr) <= 3:
        return counter + 1
    else:
        lsubp = 1
        rsubp = len(tempstr) -1

        while lsubp < rsubp:
            if tempstr[lsubp] == tempstr[rsubp] and lsubp + 1 >= rsubp:
                return counter + 1
            elif tempstr[lsubp] == tempstr[rsubp]:
                lsubp + 1
                rsubp -1
            else:
                break
    return counter

print(countSubstrings("abd"))










