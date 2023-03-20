n = int(input())
a = list(map(int, input().split()))

sorta  = sorted(a)

if sorta[-2]+sorta[-3]<=sorta[-1]:
    print("NO")
else:
    sorta[-1], sorta[-2] = sorta[-2],sorta[-1]
    print("YES")
    print(" ".join(map(str,sorta)))
