class Solution:
    def countSubstrings(self, string):

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
            if string[rp] == string[lp]:
                substring(tempstr)
                rp + 1
            elif string[rp] != string[lp]:
                rp + 1
                tempstr.append(string[rp])
            else:
                lp + 1
                rp = lp + 1
                tempstr = list(string[lp] + string[rp])
    
    def substring(self, counter, tempstr):










