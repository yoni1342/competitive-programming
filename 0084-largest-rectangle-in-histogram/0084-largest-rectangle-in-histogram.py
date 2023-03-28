class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):

                temp = stack.pop()
                left = -1 if not stack else stack[-1]
                ans = max(ans, (i-left-1)*heights[temp])
                
            stack.append(i)
        
        return ans
                