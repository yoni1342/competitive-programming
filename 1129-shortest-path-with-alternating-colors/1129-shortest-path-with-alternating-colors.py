class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for p, c in redEdges:
            graph[p].append((c,1))
        
        for p, c in blueEdges:
            graph[p].append((c,2))
        #0-1-2-0-3
        que = deque()
        visited = set()
        ans = [-1]*n
        
        que.append((0, 0))
        visited.add((0,0))
        level = 0
        while que:
            for i in range(len(que)):
                node, prevcolor = que.popleft()
                
                if ans[node] == -1:
                    ans[node] = level
            
                for neighbour, color in graph[node]:
                    if color != prevcolor and (neighbour, color) not in visited:
                        que.append((neighbour, color))
                        visited.add((neighbour, color))
                
            level += 1
        
        return ans