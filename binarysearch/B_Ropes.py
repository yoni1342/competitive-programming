n,k = list(map(int, input().split()))


a = []
for i in range(n):
    a.append(int(input()))

def check(x):
    s = 0
    for i in a:
        s += i//x
    return s >= k

l = 0
r = 1e8

for i in range(100):
    mid = l+(r-l)/2

    if check(mid):
        l = mid
    else:
        r = mid

print(l)