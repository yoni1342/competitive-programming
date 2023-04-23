class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        
        def inbound(row,col):
            return 0<=row<len(board) and 0<=col<len(board[0])
        
        def dfs(row,col,color):
            
            board[row][col] = color
            
            visited.add((row,col))
            
            for r,c in directions:
                nr = r+row
                nc = c+col
                
                if inbound(nr,nc) and (nr,nc) not in visited and board[nr][nc]=="O":
                    dfs(nr,nc,color)
                    
        
        for i in range(len(board)):
            if board[i][0] == "O" and (i, 0) not in visited:
                dfs(i,0,"O")
        for i in range(len(board)):
            if board[i][len(board[0])-1] == "O" and (i,len(board[0])-1) not in visited:
                dfs(i,len(board[0])-1,"O")
        for i in range(len(board[0])):
            if board[0][i] == "O" and (0, i) not in visited:
                dfs(0,i,"O")
        for i in range(len(board[0])):
            if board[len(board)-1][i] == "O" and (len(board)-1, i) not in visited:
                dfs(len(board)-1,i,"O")
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    dfs(i,j,"X")
        return board