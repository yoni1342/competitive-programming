class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i= 0 
        row = 0
        col = 0
        
        if numRows == 1:
            return s
        
        matrix = [[0 for _ in range(len(s))] for _ in range(numRows)]
        
        while i<len(s):
            while row<numRows and i<len(s):
                matrix[row][col] = s[i]
                row+=1
                i+=1
            if row == numRows:
                row-=2
                col+=1
                
            while row != 0 and i<len(s):
                matrix[row][col] = s[i]
                row-=1
                col+=1
                i+=1
        
        ans  = ""
        for i in range(numRows):
            for j in range(len(s)):
                if matrix[i][j] != 0:
                    ans += (matrix[i][j])
        return ans
                