class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def inbound(row,col):
            return 0<=row<len(mat) and 0<=col<len(mat[0])
        
        ans = [[0]*len(mat[0]) for _ in range(len(mat))]
        que = deque()
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    que.append((i,j))
        
        while que:
            
            for i in range(len(que)):
                row, col = que.popleft()
                
                for dx, dy in directions:
                    nr = dx+row
                    nc = dy+col
                    
                    if not inbound(nr,nc) or mat[nr][nc] == 0:
                        continue
                    ans[nr][nc] = ans[row][col]+1
                    mat[nr][nc] = 0
                    que.append((nr,nc))
                  
        return ans
            