class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) : 
            if nums[i]-1 <= len(nums) and nums[i]-1 != i and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i]  = temp
                i -= 1
            i+=1
        
        for i in range(len(nums)) :
            if nums[i] != i+1 :
                return [nums[i],i+1]