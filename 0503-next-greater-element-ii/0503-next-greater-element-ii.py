class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ref = nums[:]+nums[:]
        
        stack = []
        res = [-1]*len(nums)
        
        for i in range(len(ref)):
            
            while stack and  nums[stack[-1]%len(nums)] < ref[i]:
                res[stack.pop() % len(nums)] = ref[i]
            
            stack.append(i)
        
        return res