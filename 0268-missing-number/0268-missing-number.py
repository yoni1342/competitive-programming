class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique = set(nums)
        
        for i in range(len(nums)+1):
            if i not in unique:
                return i