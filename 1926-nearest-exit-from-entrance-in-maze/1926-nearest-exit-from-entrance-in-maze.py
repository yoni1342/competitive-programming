class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([(entrance[0],entrance[1],0)])
        
        def inbound(row, col):
            return 0<=row<len(maze) and 0<=col<len(maze[0])
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        
        while que:
            
            for i in range(len(que)):
                row,col,level = que.popleft()
                
                for dx,dy in directions:
                    nr,nc = row+dx, col+dy
                    
                    if row != entrance[0] or col!=entrance[1]:
                        if not inbound(nr,nc):
                            return level
                    
                    if inbound(nr,nc) and (nr,nc) not in visited and maze[nr][nc] == '.':
                        visited.add((nr,nc))
                        que.append((nr,nc,level+1))
        return -1
                        