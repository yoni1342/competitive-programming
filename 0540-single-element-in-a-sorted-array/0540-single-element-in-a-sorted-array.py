class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (right+left)//2
            
            if mid%2 == 0 and nums[mid] != nums[mid+1]:
                    right = mid
            elif mid%2!=0 and nums[mid] != nums[mid-1]:
                    right = mid
            else:
                left = mid+1
            
        return nums[left]