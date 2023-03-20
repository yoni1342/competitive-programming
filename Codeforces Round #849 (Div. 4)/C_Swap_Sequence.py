n = int(input())

a = list(map(int, input().split()))

num_swap = 0
swaps = []

for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if a[j]<a[min]:
            min = j
    if min!=i:
        num_swap+=1
        swaps.append([i, min])
        a[i], a[min] = a[min], a[i]

print(num_swap)
for i in range(num_swap):
    print(swaps[i][0], swaps[i][1])
            