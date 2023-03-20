tt = int(input())

while(tt):
    n = int(input())
    a = list(map(int, input().split()))
    sorta = sorted(a)
    base = [sorta[-2], sorta[-1]]

    sorta = sorta[:-2]
    Min = min(base)-1
    
    if len(sorta)>Min:
        print(Min)
    else:
        print(len(sorta))
    
    tt-=1