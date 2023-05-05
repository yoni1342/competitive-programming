class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        que = deque()
        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))
            que.append((r,c,0))
            for dx,dy in directions:
                nr, nc = r+dx, c+dy
                
                if inbound(nr,nc) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr,nc)
        
        def bfs():
            while que:
                r,c,level = que.popleft()

                for dx,dy in directions:
                    nr,nc = dx+r, dy+c

                    if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] == 1:
                        return level

                    if inbound(nr,nc) and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        que.append((nr,nc,level+1))
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return bfs()
        