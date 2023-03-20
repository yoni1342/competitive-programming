from itertools import accumulate
n, m = map(int, input().split())
prefix = [0]*(n+1)

for i in range(m):
    a,b = map(int, input().split())
    prefix[a]+=1
    prefix[b+1]-=1

final = set(accumulate(prefix[:-1]))

if 0 in final:
    print("YES")
else:
    print("NO")

