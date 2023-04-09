"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        
        for i in employees:
            graph[i.id].append(i.importance)            
            graph[i.id].append(i.subordinates)
        
        
        def dfs(id):
            if len(graph[id][1])==0:
                return graph[id][0]
            
            res = 0
            for i in graph[id][1]:
                res+=dfs(i)
            
            return res+graph[id][0]
        
        return dfs(id)