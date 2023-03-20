tt = int(input())
while(tt):

    n = int(input())
    a = list(map(int, input().split()))
    sorta = sorted(a)
    ans = 0
    i = 0
    while i<n:
        if i+1<n and sorta[i] == sorta[i+1]:
            ans+=sorta[i]
            i = i+2
            continue
        else:
            ans+=1
            i+=1
    print(ans)
    tt-=1