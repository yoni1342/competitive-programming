class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()
        
        stack = []
        stack.append(source)
        
        while stack:
            
            curr = stack.pop()
            visited.add(curr)
            
            if curr == destination:
                return True
            
            for i in graph[curr]:
                if i not in visited:
                    stack.append(i)
        
        return False