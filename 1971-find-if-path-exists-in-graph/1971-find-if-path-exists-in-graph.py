class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i:i for i in range(n)}
        rank = [1 for _ in range(n)]
        
        def find(x):
            if x == rep[x]:
                return x
            
            r = find(rep[x])
            rep[x] = r
            return r
        
        def union(x, y):
            repX = find(x)            
            repY = find(y)
            
            if repX != repY:
                
                if rank[repX] >= rank[repY]:
                    rep[repY] = repX
                    rank[repX] += rank[repY]
                else:
                    rep[repX] = repY
                    rank[repY] += rank[repX]
        
        for n1, n2 in edges:
            union(n1, n2)
        
        return find(source) == find(destination)
    