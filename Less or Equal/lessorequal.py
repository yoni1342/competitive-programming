n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
a.sort()

ans = 0

if k == 0:
    ans = a[0]-1
else:
    ans = a[k-1]

count = 0

for i in range(n):
    if a[i] <= ans:
        count += 1

if count!=k or ans<1:
    print(-1)
else:
    print(ans)
