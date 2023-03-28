class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        count = 0
        
        for i in height:
            
            while stack and stack[0] <= i:
                count += stack[0] - stack.pop()
            
            stack.append(i)
        
        while stack:
            temp = stack.pop()
            
            while stack and stack[-1]<temp:
                count += temp - stack[-1]
                stack.pop()
        
        return count