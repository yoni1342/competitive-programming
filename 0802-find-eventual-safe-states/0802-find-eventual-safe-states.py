class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0]*len(graph)
        ans = []
        def dfs(node):
            color[node] = 1
            
            for i in graph[node]:
                if color[i] == 2:
                    continue
                elif color[i] == 1:
                    return False
                else:
                    if not dfs(i):
                        return False
            
            ans.append(node)
            color[node] = 2
            return True
        
        
        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i)
        
        ans.sort()
        return ans
            