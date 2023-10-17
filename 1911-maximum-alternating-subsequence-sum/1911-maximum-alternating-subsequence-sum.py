class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(i: int, p: bool) -> int:
            if i>=n:
                return 0 
			
            if (i, p) in memo:
                return memo[(i, p)]
            num = nums[i] if p else -nums[i]
            choose = num + dp(i+1, not p)
            notchoose = dp(i+1, p)
            
            memo[(i, p)] = max(choose, notchoose)
            
            return memo[(i, p)]

        return dp(0, True)