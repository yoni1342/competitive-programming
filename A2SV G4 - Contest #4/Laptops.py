n = int(input())
laptops = []

while n:
    laptops.append(list(map(int, input().split())))
    n-=1

laptops.sort()
flag = "Poor Alex"
for i in range(1,len(laptops)):
    if laptops[i-1][1]>laptops[i][1]:
        flag = "Happy Alex"
        break
print(flag)

