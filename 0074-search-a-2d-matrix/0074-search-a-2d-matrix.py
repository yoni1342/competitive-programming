class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = len(matrix)-1
        n = len(matrix)
        m = len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for i in range(n):
            if matrix[i][0] == target:
                return True
            if matrix[i][0]>target:
                index = i-1
                break
        for j in range(m):
            if matrix[index][j] == target:
                return True
        
        return False