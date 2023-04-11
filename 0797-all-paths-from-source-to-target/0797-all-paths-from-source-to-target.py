class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        n = len(g)
        
        graph = defaultdict(list)
        
        for i in range(len(g)):
            for j in g[i]:
                graph[i].append(j)
        
        ans = []
        visited = set()
        
        def dfs(v, path):
            if v == n-1:
                ans.append(path)
            
            for i in graph[v]:
                dfs(i, path+[i])
        
        dfs(0,[0])
        return ans