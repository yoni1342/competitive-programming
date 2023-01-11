class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        left=0
        right = 0
        
        while left<len(nums):
            if nums[left]==0:
                right = left
                while right<len(nums) and nums[right]==0:
                    right+=1
                if right<len(nums):
                    nums[left], nums[right] = nums[right], nums[left]
                
            left+=1
        
        return nums