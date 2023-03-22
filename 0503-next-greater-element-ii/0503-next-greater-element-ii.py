class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        res = [-1]*len(nums)
        
        for i in range(2*len(nums)):
            
            while stack and  nums[stack[-1]%len(nums)] < nums[i%len(nums)]:
                res[stack.pop() % len(nums)] = nums[i%len(nums)]
            
            stack.append(i)
        
        return res