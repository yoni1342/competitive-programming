class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(cur,prev, path):
            if cur>=len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if i not in prev :
                    prev.add(i)
                    path.append(nums[i])
                    backtrack(cur+1,prev,path)
                    prev.remove(i)
                    path.pop() 
        backtrack(0,set(),[])
        return ans  