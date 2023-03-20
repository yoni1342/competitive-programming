from collections import Counter
tt = int(input())
while tt:
    tt-=1
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)

    l = 0
    validlen = 0

    while l<len(a):
        
        if count[a[l]]>1:
            validlen = len(a)-l-1
            count[a[l]]-=1
        l+=1
    if validlen>0:
        print(len(a)-validlen)
    else:
        print(0)