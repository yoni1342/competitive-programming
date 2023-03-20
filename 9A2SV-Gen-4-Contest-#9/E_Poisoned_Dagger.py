tt = int(input())

while tt:
    tt-=1

    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    def Check(k):
        temp = k
        for i in range(len(a)-1):
            temp += min(k, a[i+1]-a[i])
        
        return temp >= h

    l = -1
    r = h+1

    while l+1 < r:
        mid = (r+l)//2

        if Check(mid):
            r = mid
        else:
            l = mid

    print(r)