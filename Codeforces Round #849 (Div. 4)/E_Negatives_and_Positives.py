tt = int(input())

while tt:
    tt-=1
    n = int(input())
    nums = list(map(int, input().split()))
    i=0
    Min = nums[0]+nums[1]
    while i<n-1:
        Min = min(Min, nums[i]+nums[i+1])
        i+=1
    
    Sum = sum(nums)
    
    Min = -1*Min*2
    ans = Sum + Min

    if Sum>ans:
        print(Sum)
    else:
        print(ans)