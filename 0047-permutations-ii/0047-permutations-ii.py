class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(cur,prev, path):
            if cur>=len(nums):
                ans.add(tuple(path[:]))
                return
            
            for i in range(len(nums)):
                if i not in prev :
                    prev.add(i)
                    backtrack(cur+1,prev, path+[nums[i]])
                    prev.remove(i)
                    
        backtrack(0,set(),[])
        return ans  