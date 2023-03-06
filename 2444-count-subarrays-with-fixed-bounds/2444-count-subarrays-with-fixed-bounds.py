class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = -1
        min_ = max_ = -1 
        res = 0
        
        for right in range(len(nums)):
            
            if nums[right]<minK or nums[right]>maxK:
                left = right
            
            if nums[right] == minK:
                min_ = right
        
            if nums[right] == maxK:
                max_ = right
            
            if min_ >= 0 and max_ >= 0:
                res += max(0,min(min_,max_)-left)
            
        return res