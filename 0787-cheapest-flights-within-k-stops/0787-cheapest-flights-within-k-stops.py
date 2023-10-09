class Solution:
    def findCheapestPrice(self, n: int, edges: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        m = len(edges)
        for i in range(m):
            u, v, w = edges[i]
            adj[u].append((v, w))

        @lru_cache(None)
        def dp(u, k):
            if u == dst: return 0 
            if k == 0: return math.inf 
            ans = math.inf 
            for v, w in adj[u]: 
                ans = min(ans, w+dp(v, k-1))
            return ans 

        ans = dp(src, k+1)
        return ans if ans != math.inf else -1 