class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        numsLessTarget = 0
        countOfTarget = 0
        
        for i in nums:
            if i==target:
                countOfTarget+=1
            elif i<target:
                numsLessTarget+=1
        
        for i in range(numsLessTarget, numsLessTarget+countOfTarget):
            ans.append(i)
            
        return ans
