n = int(input())

a = list(map(int, input().split()))
a.sort()

if a[0] == a[-1]:
    print(-1)
else:
    print(*a)