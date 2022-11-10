class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        while l<len(nums):
            r,Min = l,l
            while r<len(nums):
                if nums[r]<nums[Min]:
                    Min = r
                r+=1
            nums[l],nums[Min] = nums[Min], nums[l]
            l+=1