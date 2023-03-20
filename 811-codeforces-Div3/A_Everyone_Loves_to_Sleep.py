tt = int(input())
while tt:
    tt-=1
    n, H, M = list(map(int,input().split()))
    sleep = (H*60) + M

    alarms = []

    for _ in range(n):
        h,m = list(map(int,input().split()))
        alarms.append((h*60)+m)

    small = float('inf')
    for i in alarms:
        if i<sleep:
            small = min(small,(i+1440)-sleep)
        else:
            small = min(small, i-sleep)
            
    print(small//60, small%60)