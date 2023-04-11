class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        
        
        def dfs(node, col):
            if color[node] != -1 and color[node] != col:
                return False
            if color[node] == -1:
                color[node] = col
                for v in graph[node]:
                    found = dfs(v, int(not(col)))
                    if not found:
                        return False
            return True
                
        
        
        for node in range(len(graph)):
            if color[node] == -1:
                found = dfs(node, 0)
                if not found:
                    return False
        return True