class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        if obstacleGrid[-1][-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        
        mimo = [[0]*(m+1) for _ in range(n+1)]
        mimo[n-1][m-1] = 1
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i!=n-1 or j!=m-1:
                    if obstacleGrid[i][j] == 1:
                        mimo[i][j] = 0
                    else:
                        mimo[i][j] = mimo[i+1][j]+mimo[i][j+1]
        
        return mimo[0][0]