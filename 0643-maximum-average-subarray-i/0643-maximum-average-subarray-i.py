class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Sum = 0
        for i in range(k):
            Sum+=nums[i]
        
        ans = Sum 
        
        for i in range(k, len(nums)):
            Sum = Sum + nums[i] - nums[i-k]
            ans = max(Sum, ans)
        
        return ans/k