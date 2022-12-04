class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)]for j in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        
        count = 1
        
        while top<bottom and left<right:
            for i in range(left, right):
                ans[top][i] = count
                count+=1
            top+=1
            for i in range(top, bottom):
                ans[i][right-1] = count
                count+=1
            right-=1
            for i in range(right-1, left-1,-1):
                ans[bottom-1][i] = count
                count+=1
            bottom-=1
            for i in range(bottom-1, top-1, -1):
                ans[i][left] = count
                count+=1
            left+=1
        return ans