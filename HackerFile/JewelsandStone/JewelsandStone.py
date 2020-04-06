def numJewelsInStones(J, S):
    ans = []
    for jewel in J:
       count = S.count(jewel)
       ans.append(count)
       answer = sum(ans)
       
    return answer

print(numJewelsInStones("aBcd", "aabCdd"))

