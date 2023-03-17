class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(path, cur):
            ans.add(tuple(sorted(path[:])))
            if cur>=len(nums):
                return
            for i in range(cur, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
                
        backtrack([], 0)
        return ans