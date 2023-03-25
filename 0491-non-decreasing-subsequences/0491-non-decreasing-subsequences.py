class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def back(idx, path):
            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                if nums[i] >= path[-1]:
                    path.append(nums[i])
                    if tuple(path) not in ans:
                        ans.add(tuple(path))
                    back(i+1, path)
                    path.pop()
        
        for i in range(len(nums)):
            back(i+1, [nums[i]])
        
        return ans