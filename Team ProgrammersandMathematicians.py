tt = int(input())
while tt:
    tt-=1
    
    a,b = map(int, input().split())
    print(min(min(a,b), (a+b)//4))
