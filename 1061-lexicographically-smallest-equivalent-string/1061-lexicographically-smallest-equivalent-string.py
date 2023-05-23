class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
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
                
                if ord(repX) <= ord(repY):
                    rep[repY] = repX
                else:
                    rep[repX] = repY
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        ans = []
        
        for i in baseStr:
            ans.append(find(i))
        
        return ''.join(ans)