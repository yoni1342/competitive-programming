class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0]*(len(nums)+1)
        Hash = {}
        count = 0
        
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        
        for i in prefix:
            if i%k in Hash:
                count += Hash[i%k]
                Hash[i%k]+=1
            else:
                Hash[i%k] = 1
        
        return count
                
                