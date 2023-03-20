tt = int(input())

while(tt):
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])
    tt-=1