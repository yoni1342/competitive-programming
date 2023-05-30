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
            res = float('inf')
            for i in coins:
                res = min(res, dfs(i+num)+1)
            dp[num] = res
            return res
        
        res = float('inf')
        for i in coins:
            res = min(res, dfs(i)+1)
        return -1 if res==float('inf') else res
    
        
            