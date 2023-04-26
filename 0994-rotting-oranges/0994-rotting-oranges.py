class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def inbound (row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        rotten = deque()
        ans = 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
                    
        while rotten and cnt > 0:
            ans += 1
            
            
            for _ in range(len(rotten)): 
                row, col = rotten.popleft() 
                
                for r, c in directions:
                    nr = row + r
                    nc = col + c

                    if inbound(nr,nc) and grid[nr][nc] == 1 :                    
                        grid[nr][nc] = 2
                        cnt -= 1
                        rotten.append((nr,nc))
                    
        
        return ans if cnt == 0 else -1