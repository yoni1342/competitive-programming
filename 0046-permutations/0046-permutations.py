class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        tester = 0
        
        def back(idx):
            nonlocal tester
            if idx == len(nums):
                ans.append(path[:])
                return 
            
            for i in range(len(nums)):
                if (1<<i) & tester == 0:
                    tester |= 1<<i
                    path.append(nums[i])
                    back(idx+1)
                    path.pop()
                    tester &= ~(1<<i)
        
        back(0)
        return ans