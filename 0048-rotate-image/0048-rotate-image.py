class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        
        for layer in range(length//2):
            n = length-1
            loop = n-(2*layer)
            
            for ele in range(loop):
                row = layer
                col = ele+layer
                prev = matrix[row][col] 
                
                for _ in range(4):
                    # the next cordinate after we rotate for (row, col) is (col, n-row)
                    val = matrix[col][n-row]
                    matrix[col][n-row] = prev
                    prev = val
                    
                    temp = col
                    col = n-row
                    row = temp
        
        return matrix