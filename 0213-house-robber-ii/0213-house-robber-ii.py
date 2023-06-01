class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robbb(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            dp = []
            dp.append(nums[0])
            dp.append(max(nums[0], nums[1]))

            for i in range(2,len(nums)):
                dp.append(max((nums[i]+dp[-2]), dp[-1]))

            return dp[-1]
        
        return max(robbb(nums[1:]), robbb(nums[:-1]))