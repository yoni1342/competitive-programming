tt = int(input())

while tt:
    tt-=1
    
    a,b,c = list(map(int, input().split()))

    if b>=c:
        if a<b:
            print(1)
        elif a>b:
            print(2)
        else:
            print(3)
    else:
        time = (abs(b-c)*2)+abs(b)
        if a<time:
            print(1)
        elif a>time:
            print(2)
        else:
            print(3)