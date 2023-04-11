class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        # 1:[2,3]     1:[2,3]
        # 2:[1,3]     2:[1,4]
        # 3:[1,2]     3:[1]
        #             4:[2]
        
#         f = [1] 
#         s = [2,3]
        graph = defaultdict(list)
        
        for i in dislikes:
            graph[i[0]].append(i[1])            
            graph[i[1]].append(i[0])
        
        color = [-1]*n
        
        def dfs(node, col):
            if color[node-1] != -1 and color[node-1] != col:
                return False
            elif color[node-1] == -1:
                color[node-1] = col
                
                for i in graph[node]:
                    found = dfs(i, int(not(col)))
                    if not found:
                        return False
            return True
        
        for i in graph:
            if color[i-1] == -1:
                found = dfs(i, 0)
                if not found:
                    return False
        return True