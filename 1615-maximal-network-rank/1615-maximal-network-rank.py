class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        
        res = 0
        
        for i in graph:
            for j in graph:
                
                if i!=j:
                    
                    if i in graph[j]:
                        res = max(res, len(graph[i]+graph[j])-1)
                    else:
                        res =max(res, len(graph[i]+graph[j]))
        
        return res