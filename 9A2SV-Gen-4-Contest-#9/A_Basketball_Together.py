n, d = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

l = 0
r = len(a)-1

ans = 0
while l<=r:
    count = 1
    while l<r and a[r]*count <= d:
        l+=1    
        count+=1
    if a[r]*count > d:
        ans+=1
    r-=1

print(ans)