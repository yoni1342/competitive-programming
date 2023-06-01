class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n==1:
            return 1
        mimo = defaultdict(int)
        
        for i in range(n, 0, -1):
            self.dfs(i, mimo)
        
        return max(mimo.values())
    
    
    def dfs(self, n, mimo):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n in mimo:
            return mimo[n]
        if n%2 == 0:
            mimo[n] = self.dfs(n//2, mimo)
        else:
            mimo[n] = self.dfs(n//2, mimo) + self.dfs(n//2 + 1, mimo)
        
        return mimo[n]