class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, cur):
            if cur>=len(nums):
                ans.append(path[:])
                return
            for i in range(cur, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
            backtrack(path, i+1)
            
        backtrack([], 0)
        return ans