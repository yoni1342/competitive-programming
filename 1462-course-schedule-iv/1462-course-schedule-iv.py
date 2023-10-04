class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[float('inf')] * numCourses for _ in range(numCourses)]
        
        for i, j in prerequisites:
            dist[i][j] = 1
        
        for i in range(numCourses):
            dist[i][i] = 0
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        ans = []
        for i, j in queries:
            if dist[i][j] == float("inf"):
                ans.append(False)
            else:
                ans.append(True)
        return ans