n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
q = list(map(int, input().split()))


for x in q:
    l = -1
    r = n

    while l < r-1:
        mid = l+(r-l)//2

        if a[mid]>=x:
            r = mid
        else:
            l = mid

    print(r+1)