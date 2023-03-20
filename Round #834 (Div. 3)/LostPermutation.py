tt = int(input())

for i in range(tt):
    m, s = map(int, input().split())
    b = set(map(int, input().split()))

    i = 1
    Sum = 0
    while Sum<s:
        if i not in b:
            Sum+=i
            b.add(i)
        i+=1
    if Sum == s and len(b) == max(b):
        print("YES")
    else:
        print("NO")