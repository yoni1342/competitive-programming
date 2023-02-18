n = int(input())
arr = list(map(int, input().split()))
oddeven = [False, False]

for i in range(n):
    if arr[i] % 2 == 0:
        oddeven[0] = True
    else:
        oddeven[1] = True

if oddeven[0] and oddeven[1]:
    arr.sort()

for i in range(n):
    print(arr[i], end=" ")
