class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)-1
        
        ans = 0
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i-j == 0 or i+j == n:
                    ans+=mat[i][j]
                    print(ans)
        
        return ans