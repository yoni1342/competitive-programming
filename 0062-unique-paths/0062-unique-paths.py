class Solution:
    def uniquePaths(self, m: int, n: int, mimo = {}) -> int:
        if m==0 or n==0:
            return 0
        
        if m==1 and n == 1:
            return 1
        
        if (n, m) in mimo:
            return mimo[(n,m)]
        
        mimo[(n,m)] = self.uniquePaths(m-1, n, mimo) + self.uniquePaths(m, n-1, mimo)
        return mimo[(n,m)]