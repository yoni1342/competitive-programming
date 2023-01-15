class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = set()
        row = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        