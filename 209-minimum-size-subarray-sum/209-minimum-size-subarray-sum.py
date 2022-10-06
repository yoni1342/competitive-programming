import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0
        right =0
        Min = math.inf
        Sum = 0
        while right<len(nums):
            Sum+=nums[right]
            while Sum>=target:
                Min = min(Min, (right-left)+1)
                Sum-=nums[left]
                left+=1
            right+=1
        if Min==math.inf:
            Min=0
        return Min