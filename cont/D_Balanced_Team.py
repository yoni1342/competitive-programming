n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0

p=0
for i in range(n):
    while p<n and a[p]-a[i]<=5:
        ans = max(ans, p+1-i)
        p+=1

print(ans)