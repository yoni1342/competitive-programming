class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        income = [0]*numCourses
        ans = []
        
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            income[c1]+=1
        
        
        que = deque()
        
        for i in range(len(income)):
            if income[i] == 0:
                que.append(i)
        
        while que:
            course = que.popleft()
            ans.append(course)
            
            for neighbour in graph[course]:
                income[neighbour]-=1
                if income[neighbour] == 0:
                    que.append(neighbour)
        
        if len(ans) != numCourses:
            return False
        return True
                