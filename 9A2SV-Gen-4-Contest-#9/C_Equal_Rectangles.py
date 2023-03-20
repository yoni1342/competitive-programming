tt = int(input())
while tt:
    tt-=1

    n = int(input())
    a = list(map(int, input().split()))
    a.sort()


    flag = "YES"
    l = 0
    r = 1
    
    while r<len(a):
        if a[l]!=a[r]:
            flag = "NO"
            break
        l+=2
        r+=2
    if flag == "NO":
        print(flag)
        continue
    l = 0
    r = len(a)-1

    area = a[0]*a[-1]
    while l<=r:
        if a[l]*a[r]!=area:
            flag = "NO"
            break
        l+=1
        r-=1
    print(flag)