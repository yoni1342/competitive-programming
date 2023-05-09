class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # white = 0, gray = 1, black = 2
        color = [0]*numCourses
        ans = []
        
        for i in prerequisites:
            graph[i[1]].append(i[0])
        
        def dfs(node):
            
            color[node] = 1
            
            for curnode in graph[node]:
                col = color[curnode]
                
                if col == 0:
                    if not dfs(curnode):
                        return False
                elif col == 1:
                    return False
                else:
                    continue
                    
            color[node] = 2
            ans.append(node)
            return True

        for node in range(numCourses):
            
            if color[node] != 0:
                continue
            
            if not dfs(node):
                return []
            
        return ans[::-1]