import math
tt = int(input())
while(tt):
    n = int(input())
    a = list(map(int, input().split()))
    Max = max(a)
    Min = min(a)
    increasingList = [Min, Max]
    decreasingList = [Min, Max]

    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            avg = math.ceil((a[i]+a[i+1])/2)
            if increasingList[0]<avg:
                increasingList[0] = avg
        elif a[i]<a[i+1]:
            avg = math.floor((a[i]+a[i+1])/2)
            if decreasingList[1]>avg:
                decreasingList[1] = avg        
    
    if increasingList[0]>decreasingList[1]:
        print(-1)
    else:
        print(increasingList[0])
    tt-=1
