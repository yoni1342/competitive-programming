n, a, b = map(int, input().split())
arr = list(map(int, input().split()))


left =0
count = 0
Sum = 0

flag = False
for i in range(n):
    Sum += arr[i]
    if Sum >= a and Sum<=b:
        count += 1
    while Sum >= b:
        Sum -= arr[left]
        left += 1
        flag = True
    if flag and a<=Sum<=b:
        count += 1
        flag = False

print(count)