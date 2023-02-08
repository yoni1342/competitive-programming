class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = [0]*len(nums)
        
        for i in range(len(nums)):
            jumps[i] = i+nums[i]
        
        i = len(nums)-1
        count = 0
        
        while i>0:
            i = self._calculateMinIndex(jumps, i)
            count+=1    
        
        return count
    
    def _calculateMinIndex(self,jumps, target):
        res = 0
        
        for i in range(target,-1, -1):
            if jumps[i]>= target:
                res = i
        return res