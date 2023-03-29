class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                temp = stack.pop()
                ans[temp] += 1
                if stack:
                    ans[stack[-1]]+=1
            
            stack.append(i)
        if stack:
            for i in range(len(stack)-2, -1, -1):
                ans[stack[i]]+=1
        return ans