class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def back(idx, path,Sum):
            if Sum == target:
                ans.append(path[:])
                return
            if Sum > target or idx>=len(candidates):
                return
            
            
            for i in range(idx,len(candidates)):
                back(i, path+[candidates[i]], Sum+candidates[i])
        
        back(0, [], 0)
        
        return ans