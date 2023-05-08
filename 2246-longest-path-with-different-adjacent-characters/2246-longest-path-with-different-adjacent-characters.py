class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i in range(1,len(parent)):
            graph[parent[i]].append(i)

        ans = 1
        
        def dfs(node):
            nonlocal ans
            
            long,short = 0,0
            
            for i in graph[node]:
                path_len = dfs(i)
                
                if s[node]!=s[i]:
                    
                    if path_len > long:
                        short = long
                        long = path_len
                    elif path_len > short:
                        short = path_len
            
            ans = max(ans, long+1+short)
            
            return long+1
        
        dfs(0)
        return ans