import sys
sys.setrecursionlimit(100000)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(int)
        
        def back(idx, Sum):
            if idx >= len(nums):
                if Sum == target:
                    return 1
                return 0

            if (idx,Sum) in memo:
                return memo[(idx,Sum)]
            
            memo[(idx,Sum)] = back(idx+1, Sum - nums[idx]) + back(idx+1, Sum+nums[idx])
            return memo[(idx,Sum)]
        return back(0, 0)
        