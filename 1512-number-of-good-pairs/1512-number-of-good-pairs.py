class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n-1):
            j = i+1
            while j < n:
                if nums[i] == nums[j]:
                    count += 1
                j += 1
        return count