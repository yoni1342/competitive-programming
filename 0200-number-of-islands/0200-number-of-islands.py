class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(i, j):
            grid[i][j] = 1
            
            if i>0 and grid[i-1][j] == '1':
                helper(i-1, j)
            if j>0 and grid[i][j-1] == '1':
                helper(i, j-1)
            if i<len(grid)-1 and grid[i+1][j] == "1":
                helper(i+1, j)
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                helper(i, j+1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    ans+=1
                    helper(i, j)
        
        return ans