class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph)
        visited = set()
        def Color(v, col):
            if col == 1:
                color[v] = -1
            else:
                color[v] = 1
        
        def dfs(v):
            visited.add(v)
            for i in graph[v]:
                if color[i] == color[v]:
                    return False
                Color(i, color[v])
            
            for i in graph[v]:
                if i not in visited:
                    found = dfs(i)
                    if not found:
                        return False
            return True
        
        for i in range(len(graph)):
            if color[i] == 0:
                color[i] = 1
            if i not in visited:
                found = dfs(i)
                if not found:
                    return False
        return True
     