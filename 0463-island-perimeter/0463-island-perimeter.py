class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        
        res = 0        
        visited = set()
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        
        
        def dfs(row, col):
            nonlocal res
            if (row, col) not in visited:
                visited.add((row, col))
                
                for nextrow, nextcol in directions:
                    newrow = row + nextrow
                    newcol = col + nextcol
                    
                    if not inbound(newrow, newcol) or grid[newrow][newcol] == 0:
                        res+=1
                    else:
                        dfs(newrow, newcol)
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return res