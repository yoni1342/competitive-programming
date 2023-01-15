class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0 , len(matrix)-1
        
        while left<right:
            
            for i in range(right-left):
                top, buttom = left, right
                
                topleft = matrix[top][left+i]
                
                matrix[top][left+i] = matrix[buttom-i][left]
                matrix[buttom-i][left] = matrix[buttom][right-i]
                matrix[buttom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topleft
            
            left+=1
            right-=1