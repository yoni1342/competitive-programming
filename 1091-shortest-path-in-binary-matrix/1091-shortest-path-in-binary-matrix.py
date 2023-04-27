class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        directions = [(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        que = deque([(0,0,1)])
        visited = set([(0,0)])
        
        while que:
            
            flag = False
            for _ in range(len(que)):
                row,col,level = que.popleft()
                if row == len(grid)-1 and col == len(grid)-1:
                    return level
                
                for r,c in directions:
                    nr,nc = row+r, col+c
                    
                    if inbound(nr,nc) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        que.append((nr,nc,level+1))
                        
            
        return -1