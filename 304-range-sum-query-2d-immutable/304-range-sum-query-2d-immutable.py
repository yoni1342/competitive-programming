class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for j in range(len(matrix[0])+1)]for i in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.prefix[i][j+1] = self.prefix[i][j]+matrix[i][j]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        Sum = 0
        i = row1
        while i<=row2:
            Sum += (self.prefix[i][col2+1] - self.prefix[i][col1])
            i+=1
        return Sum
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)