class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        
        def dfs(node, flag):
            if node >= len(prices):
                return 0
        
            if (node,flag) in memo:
                return memo[(node,flag)]
            
            if flag == 0:
                memo[(node,flag)] = max(dfs(node+1, 1) - prices[node], dfs(node+1, 0))
            else:
                memo[(node, flag)] = max(dfs(node+1,0) + prices[node]-fee, dfs(node+1, 1))
            
            return memo[(node,flag)]
        
        return max(dfs(0,0), dfs(0,1) - prices[0])