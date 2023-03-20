n, m = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
p1 = 0
for i in range(m):
    while p1<n and a1[p1]<a2[i]:
        p1+=1
    print(p1, end=" ")