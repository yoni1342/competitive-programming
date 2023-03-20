from collections import defaultdict
tt = int(input())
while tt:
    tt-=1
    n = int(input())

    s = list(input())
    
    zHash = defaultdict(set)
    oHash = defaultdict(set)

    f = 0
    
    for i in range(len(s)):
        zHash[s[i]].add((f))
        oHash[s[i]].add(int(not f))
        f = int(not f)
    
    flag = "YES"

    for i in zHash:
        if len(zHash[i])>1:
            flag = "NO"
            break
    
    for i in oHash:
        if len(oHash[i])>1:
            flag = "NO"
            break
    
    print(flag)