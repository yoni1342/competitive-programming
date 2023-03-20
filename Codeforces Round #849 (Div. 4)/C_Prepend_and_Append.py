tt = int(input())

while tt:
    n = int(input())
    a = input()
    p1 = 0
    p2 = n-1
    flag = 0
    while p1<=p2:
        if a[p1] == a[p2]:
            flag = (p2-p1)+1
            break
        p1+=1
        p2-=1
    print(flag)
    tt-=1