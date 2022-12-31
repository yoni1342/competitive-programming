class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        
        cur_row=0
        cur_col=0
        
        answer = []
         
        n = len(mat)
        m = len(mat[0])
        
        
        while len(answer) != m*n:
            
            if up:
                while cur_row >= 0 and cur_col < m:
                    answer.append(mat[cur_row][cur_col])
                    
                    cur_row -= 1
                    cur_col +=1
                
                if cur_col == m:
                    cur_row += 2
                    cur_col -= 1
                else:
                    cur_row +=1
                up = False
                
            else:
                while cur_col >= 0 and cur_row < n:
                    answer.append(mat[cur_row][cur_col])
                    
                    cur_row += 1
                    cur_col -= 1
                    
                if cur_row == n:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                
                up = True
        return answer