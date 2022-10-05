class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        maxOne = 0
        left = 0
        right = 0
        
        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if left<len(nums) and nums[left]==0:
                    zeros-=1
                left+=1
            maxOne = max(maxOne, right-left+1)
            right+=1
        return maxOne