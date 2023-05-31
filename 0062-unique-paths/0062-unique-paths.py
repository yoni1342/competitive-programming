class Solution:
    def uniquePaths(self, m: int, n: int, mimo = {}) -> int:
        mimo = [[0]*n for _ in range(m)]
        
        for i in range(n):
            mimo[0][i] = 1
        for i in range(m):
            mimo[i][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                mimo[i][j] = mimo[i-1][j] + mimo[i][j-1]
        
        return mimo[m-1][n-1]