n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = []
p1 = 0
p2 = 0

while p1<n and p2<m:
    if a[p1] < b[p2]:
        ans.append(a[p1])
        p1 += 1
    else:
        ans.append(b[p2])
        p2 += 1

while p1<n:
    ans.append(a[p1])
    p1 += 1

while p2<m:
    ans.append(b[p2])
    p2 += 1

print(*ans)
