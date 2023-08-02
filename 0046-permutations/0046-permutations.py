class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        prev = set()
        
        def back(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return;
            
            for i in range(len(nums)):
                if nums[i] not in prev:
                    path.append(nums[i])
                    prev.add(nums[i])
                    back(path)
                    prev.remove(path.pop())
                    
        back([])
        return ans