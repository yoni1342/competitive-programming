class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        
        def inbound(x, y):
            return 0<=x<len(heights) and 0<=y<len(heights[0])
        
        
        def bfs():
            h = [(0,0,0)]
            visited = set()
            
            while h:
                e,i,j = heapq.heappop(h)
                
                if i == n-1 and j == m-1:
                    return e
                
                if (i, j) not in visited:
                    visited.add((i,j))
                    for x, y in directions:
                        nx, ny = x+i, y+j
                        if inbound(nx, ny):
                            diff = max(e, abs(heights[i][j]-heights[nx][ny]))
                            heapq.heappush(h, (diff,nx,ny))
        
        
        return bfs()