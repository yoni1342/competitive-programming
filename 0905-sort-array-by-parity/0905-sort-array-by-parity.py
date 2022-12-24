class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        leftptr = 0
        rightptr = 0
        n = len(nums)

        while rightptr < n:
            if nums[rightptr] % 2 == 0:
                nums[rightptr], nums[leftptr] = nums[leftptr], nums[rightptr]
                leftptr+=1
            rightptr+=1
            
        return nums