class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        ans = []

        while i < len(nums):
            temp = nums[i] - 1

            if nums[temp] != nums[i]:
                nums[temp], nums[i] = nums[i], nums[temp]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return nums[i]
