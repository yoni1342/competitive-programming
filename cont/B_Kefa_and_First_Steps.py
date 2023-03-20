n = int(input())

a = list(map(int, input().split()))

Max = 0

p=1

for i in range(1,n):
    if a[i]>=a[i-1]:
        p+=1
    else:
        Max = max(Max, p)
        p=1
Max = max(Max, p)
print(Max)