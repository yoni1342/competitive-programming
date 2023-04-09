class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        def inbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        visited = set()
        ans = 0
        
        def dfs(row, col):
            
            visited.add((row,col))
            res = 0
            for rowi, coli in directions:
                nextrow = row+rowi
                nextcol = col+coli

                if inbound(nextrow, nextcol) and grid[nextrow][nextcol] == 1 and (nextrow, nextcol) not in visited:
                    res += dfs(nextrow, nextcol)
            if res:
                return res+1
            return 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans = max(ans, dfs(i, j))
        
        return ans