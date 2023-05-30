class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        dp = defaultdict(int)
        
        def dfs(num):
            if num == amount:
                return 0
            if num > amount:
                return float('inf')
            if num in dp:
                return dp[num]
            res = []
            for i in coins:
                res.append(dfs(i+num)+1)
            dp[num] = min(res)
            return min(res)
        
        res = []
        for i in coins:
            res.append(dfs(i)+1)
        return -1 if min(res)==float('inf') else min(res)
    
        
            