class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        
        incoming = [0]*n
        
        graph = defaultdict(list)
        
        for i in edges:
            graph[i[0]].append(i[1])
            incoming[i[1]]+=1
        
        que = deque()
        
        for i in range(len(incoming)):
            if incoming[i] == 0:
                que.append(i)
        
        while que:
            node = que.popleft()
            
            for neighbor in graph[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    que.append(neighbor)
                
                ans[neighbor] = ans[neighbor].union(ans[node])
                ans[neighbor].add(node)
                
        return [sorted(list(x)) for x in ans]
    