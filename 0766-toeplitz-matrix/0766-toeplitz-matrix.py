class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        digonal = defaultdict(lambda:-1)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if digonal[i-j]!=-1 and digonal[i-j]!=matrix[i][j]:
                    return False
                digonal[i-j] = matrix[i][j]
        
        return True