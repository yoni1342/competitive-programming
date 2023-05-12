 def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        indegre = defaultdict(int)
        
        for i in range(N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
            
            for j in range(min(len(s1), len(s2))):
                if s1[j] != s2[j]:
                    graph[s1[j]].append(s2[j])
                    indegre[s2[j]]+=1
                    break
        
        que = deque()
        
        for i in range(K):
            if indegre[chr(i+97)] == 0:
                que.append(chr(i+97))
        
        res = []
        while que:
            node = que.popleft()
            res.append(node)
            
            for neighbor in graph[node]:
                indegre[neighbor]-=1
                if indegre[neighbor] == 0:
                    que.append(neighbor)
        
        return ''.join(res)
