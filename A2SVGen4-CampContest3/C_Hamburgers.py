re = input().strip()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

count = {'B': 0, 'S': 0, 'C': 0}
for ch in re:
    count[ch] += 1

lo, hi = 0, int(1e14)
while lo < hi:
    mid = (lo + hi + 1) // 2
    cost = max(0, mid*count['B'] - nb)*pb \
         + max(0, mid*count['S'] - ns)*ps \
         + max(0, mid*count['C'] - nc)*pc
    if cost <= r:
        lo = mid
    else:
        hi = mid - 1

# output the result
print(lo)
