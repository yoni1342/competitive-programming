class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        res = []
        
        for num in nums:
            prefix+=num
            res.append(prefix)
        
        return res