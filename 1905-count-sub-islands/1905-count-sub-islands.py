class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        grid2Island = []
        
        visited2 = set()
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        cord = []
        def inbound(row, col):
            return 0<=row<len(grid2) and 0<=col<len(grid2[0])
        def dfs(i,j):
            visited2.add((i,j))
            cord.append((i,j))
            for r,c in directions:
                ni = i+r
                nj = j+c
                
                if (ni,nj) not in visited2 and inbound(ni, nj) and grid2[ni][nj] == 1:
                    dfs(ni, nj)
                    
        
        
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i,j) not in visited2 and grid2[i][j] == 1:
                    cord = [] 
                    dfs(i,j)
                    grid2Island.append(cord)
        print(grid2Island)
        ans = 0
        
        for i in grid2Island:
            flag = True
            for j in i:
                row,col = j
                if grid1[row][col] != 1:
                    flag = False
                    break
            if flag:
                ans+=1

        return ans