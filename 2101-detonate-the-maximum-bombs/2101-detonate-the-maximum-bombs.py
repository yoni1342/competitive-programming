class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i,val in enumerate(bombs):
            x1,y1,r1 = val
            
            for j, val in enumerate(bombs):
                if i != j:
                    x2,y2,r2 = val
                    d=(((x2-x1)**2)+((y2-y1)**2))**.5
                    if d <= r1:
                        graph[i].append(j)
        
        ans = 0
        def dfs(node,visited):
            visited.add(node)
            
            count = 0
            for i in graph[node]:
                if i not in visited:
                    count += dfs(i,visited)
            return count+1
        
        s = list(graph.keys())

        for i in s:
            ans = max(ans, dfs(i, set()))
        
        if not ans:
            return 1
        return ans