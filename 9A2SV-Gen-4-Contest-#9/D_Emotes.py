n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

total = m // (k+1)
rem = m % (k+1)

one = k*a[0]+a[1]
all = total * one + rem*a[0]

print(all)