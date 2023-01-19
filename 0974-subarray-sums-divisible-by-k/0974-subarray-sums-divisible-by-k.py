class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix = [0]*(n+1)
        Hash = {}
        
        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i] 
        
        for i in prefix:
            if i%k in Hash:
                count += Hash[i%k]
                Hash[i%k]+=1
            else:
                Hash[i%k] = 1
        return count