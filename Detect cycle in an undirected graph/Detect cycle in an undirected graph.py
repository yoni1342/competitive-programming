def isCycle(self, V: int, adj: List[List[int]]):
		#Code here
		visited = set()
        
        def dfs(node,parent):
            for neighbor in adj[node]:
                if neighbor != parent :
                    if neighbor in visited:
                        return True 
                    else:
                        visited.add(neighbor)
                        if dfs(neighbor,node):
                            return True
            return False
                    
            
        for i in range(len(adj)):
            if i not in visited:
                visited.add(i)
                res = dfs(i,-1)
                if res:
                    return res
        
        return res
