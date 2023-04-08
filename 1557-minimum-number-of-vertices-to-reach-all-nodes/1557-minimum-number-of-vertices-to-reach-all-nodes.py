class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for i in edges:
            graph[i[1]].append(i[0])
        
        ans = []
        for i in range(n):
            if len(graph[i]) == 0:
                ans.append(i)
        
        return ans