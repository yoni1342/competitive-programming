class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        row = [0]*n
        col = [0]*m
        
        ans = [[0 for i in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        for i,rowVal in enumerate(row):
            for j, colVal in enumerate(col):
                oneSum = rowVal+colVal
                zeroSum = (m-rowVal)+(n-colVal)
                
                ans[i][j] = oneSum - zeroSum
                
        return ans