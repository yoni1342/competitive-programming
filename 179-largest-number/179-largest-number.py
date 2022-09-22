class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                s1 = str(nums[j]) + str(nums[j+1])
                s2 = str(nums[j+1]) + str(nums[j])
                if int(s1) < int(s2):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        largest = ''
        for i in nums:
            largest += str(i)
        largest = int(largest)
        return str(largest)