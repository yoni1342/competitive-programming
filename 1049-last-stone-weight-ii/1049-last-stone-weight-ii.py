class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        Sum = sum(stones)
        target = math.ceil(Sum/2)
        
        @cache
        def dp(i, curr_sum):
            nonlocal Sum
            
            if i >= len(stones) or curr_sum > target:
                return abs(curr_sum-(Sum-curr_sum))
            
            return min(dp(i+1, curr_sum + stones[i]), dp(i+1, curr_sum))
        
        return dp(0, 0)