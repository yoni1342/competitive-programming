class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = float("inf")
        Sum = 0
        
        while right<len(nums):
            while right<len(nums) and Sum<target:
                Sum+=nums[right]
                right+=1
            
            while left<=right and Sum>=target:
                ans = min(ans, right-left)
                Sum -= nums[left]
                left+=1
        if ans == float('inf'):
            return 0
        return ans
        
                
             