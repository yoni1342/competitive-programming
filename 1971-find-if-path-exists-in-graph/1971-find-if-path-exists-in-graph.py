class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour)
                    
                    if found:
                        return True
                    
            return False
    
        return dfs(source)