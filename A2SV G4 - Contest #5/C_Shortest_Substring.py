from collections import defaultdict

tt = int(input())

for _ in range(tt):
    
    a = list(map(int, list(input())))
    n = len(a)
    count = defaultdict(int)
    left = 0
    right = 0
    Min = float('inf')
    while right<n:
        while right<n and len(count)<3:
            count[a[right]]+=1
            right+=1
        while len(count)==3:
            Min = min(Min, right-left)
            count[a[left]]-=1
            if count[a[left]]==0:
                del count[a[left]]
            left+=1
    if Min == float('inf'):
        print(0)
    else:
        print(Min)