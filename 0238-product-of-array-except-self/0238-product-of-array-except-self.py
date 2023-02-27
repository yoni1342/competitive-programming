class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*(len(nums)+1)
        suffix = [1]*(len(nums)+1)
        n = len(nums)
        ans = []
        
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
            suffix[i+1] = suffix[i] * nums[n-1-i]
            
        
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[n-i-1])
        
        return ans