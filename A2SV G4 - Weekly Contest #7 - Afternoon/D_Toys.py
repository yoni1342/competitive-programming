n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

toys = set()

for i in range(m):
    toys.add(input())

simmlar = m - (len(toys))

Min = 0
Max = 0


for i in range(m-simmlar):
    Min+=a[i]

temp = n-1
for i in range(m-simmlar):
    Max+=a[temp]
    temp-=1

for i in range(simmlar):
    Min+=a[0]
    Max+=a[-1]

print(Min,Max)