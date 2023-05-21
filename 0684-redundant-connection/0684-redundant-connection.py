class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i:i for i in range(1,len(edges)+1)}
        rank = [1 for _ in range(len(edges)+1)]
        
        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            repX = find(x)            
            repY = find(y)
            
            if repX == repY:
                return True
            
            if rank[repX] >= rank[repY]:
                rep[repY] = repX
                rank[repX] += rank[repY]
            else:
                rep[repX] = repY
                rank[repY] += rank[repX]
        
        for x,y in edges:
            if union(x,y):
                return [x,y]
        