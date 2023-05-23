class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {i:i for i in "abcdefghijklmnopqrstuvwxyz"}
        
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
                rep[repY] = repX
                
        
        for i in equations:
            if i[1] == "=":
                union(i[0], i[-1])
        for i in equations:
            if i[1] == "!":
                if find(i[0]) == find(i[-1]):
                    return False
        return True