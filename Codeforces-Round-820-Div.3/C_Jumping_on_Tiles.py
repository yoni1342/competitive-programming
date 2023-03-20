from collections import defaultdict
tt = int(input())
while tt:
    tt-=1

    a = list(input())
    nums = []
    for i in a:
        nums.append(ord(i))
    
    Hash = defaultdict(set)

    for i in range(len(nums)):
        Hash[nums[i]].add(i+1)
    
    mykey = list(Hash.keys())
    mykey.sort(reverse=True)
    sorted_Hash = {i: sorted(list(Hash[i])) for i in mykey}
    
    beg = end = 0
    for i in range(len(mykey)):
        if 1 in Hash[mykey[i]]:
            beg = i
        if len(nums) in Hash[mykey[i]]:
            end = i

    cost = abs(mykey[beg]- mykey[end])
    path = []

    if beg < end:
        for i in range(beg, end+1):
            path.extend(sorted_Hash[mykey[i]])
    else:
        for i in range(beg,end-1,-1):
            path.extend(sorted_Hash[mykey[i]])
    
    print(cost, len(path))
    print(*path)