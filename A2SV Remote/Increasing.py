tt = int(input())

while(tt):
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    if len(b)==len(a):
        print("Yes")
    else:
        print("No")
    
    tt-=1