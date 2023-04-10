class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def inbound(row,col):        
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row, col):
            visited.add((row,col))
            
            for rowi, coli in directions:
                nextrow = row + rowi
                nextcol = col + coli
                
                if inbound(nextrow, nextcol) and (nextrow, nextcol) not in visited and grid[nextrow][nextcol] == "1":
                    dfs(nextrow, nextcol)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    ans+=1
        
        return ans