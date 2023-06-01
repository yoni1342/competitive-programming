class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top-down
        n = len(cost)
        memo = defaultdict(int)
        
        return min(self.dfs(n-1, memo,cost), self.dfs(n-2,memo,cost))
        
    def dfs(self, n, memo,cost):
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]
        
        if n in memo:
            return memo[n]
        
        memo[n] = min(self.dfs(n-1, memo,cost), self.dfs(n-2, memo,cost))+cost[n]
        return memo[n]