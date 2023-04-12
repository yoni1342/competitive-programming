class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                    
        visited = set()
        
        def dfs(node):
            visited.add(node)
            
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        
        
        ans = 0
        
        for i in graph:
            if i not in visited:
                ans+=1
                dfs(i)
        
        return ans