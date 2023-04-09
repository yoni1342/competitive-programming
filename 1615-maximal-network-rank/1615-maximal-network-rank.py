class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        for i in graph:
            for j in graph:
                if i!=j:
                    if i in graph[j]:
                        ans = max(ans, len(graph[i]+graph[j])-1)
                    else:
                        ans = max(ans, len(graph[i]+graph[j]))
                        
        return ans