tt = int(input())

while tt:
    tt-=1
    n = int(input())
    a = input().split()
    
    p1 = 0
    p2 = n-1

    ans = []

    while p1<=p2:
        if p1 == p2:
            ans.append(a[p1])
        else:
            ans.append(a[p1])
            ans.append(a[p2])
        p1+=1
        p2-=1
    print(' '.join(ans))