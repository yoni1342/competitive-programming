tt = int(input())

while tt:
    a = list(input()) 
    p1 = 0
    p2 = 1
    res = set()
    n = len(a)
    while p1<len(a) and p2<len(a):
        if a[p1] != a[p2]:
            res.add(a[p1])
            if p2 == n-1:
                res.add(a[p2])
            p1+=1
            p2+=1
        elif a[p1] == a[p2]:
            if p2 == n-2:
                res.add(a[-1])
            p2+=2
            p1+=2
    if n==1:
        res.add(a[0])
    
    ans = sorted(res)
    print(''.join(ans))
    tt-=1
