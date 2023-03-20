import bisect
n = int(input())

s = list(input().split())
t = int(input())

for i in range(t):
    name = input()
    p = bisect.bisect_left(s, name)
    print(p)