class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        
        for i in range(len(requests)):
            start, end = requests[i]
            
            prefix[start]+=1
            prefix[end+1]-=1
        
        prefix = list(accumulate(prefix[:-1]))
        prefix = sorted(prefix, reverse = True)
        nums = sorted(nums, reverse = True)
        
        res = sum([i * j for i,j in zip(prefix, nums)])
        
        return res%(10**9 + 7)
        