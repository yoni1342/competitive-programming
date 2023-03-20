tt = int(input())

while tt:
    tt-=1
    a,b,c = list(map(int,input().split()))

    if a+b == c:
        print("+")
    elif a-b == c:
        print("-")