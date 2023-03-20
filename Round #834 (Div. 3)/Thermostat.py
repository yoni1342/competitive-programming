tt = int(input())
for i in range(tt):
    l,r,x = map(int, input().split())
    a, b = map(int, input().split())
    k = b-x
    if a == b:
        print(0)
        continue
    if a+x>r and a-x<l:
        print(-1)
        continue
    if a+x>=b:
        print(1)
        continue

    if b+x<=r:
        print(2)
    elif k>=l:
        print(3)
    else:
        print(-1)