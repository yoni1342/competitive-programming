class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        counter = 0
        
        for i in nums:
            if counter < 0:
                counter = 0            
            counter += i
            res = max(res, counter)
        return res