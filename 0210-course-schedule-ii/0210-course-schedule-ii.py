class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        income = [0]*numCourses
        order = []
        
        for i in prerequisites:
            income[i[0]]+=1
            graph[i[1]].append(i[0])
        
        que = deque()
        
        for i in range(len(income)):
            if income[i] == 0:
                que.append(i)
        
        while que:
            course = que.popleft()
            order.append(course)
            
            for neighbor in graph[course]:
                income[neighbor]-=1
                
                if income[neighbor] == 0:
                    que.append(neighbor)
            
        if len(order) != numCourses:
            return []
        
        return order
            