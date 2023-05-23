class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        
        rep = {i:i for i in range(len(s))}
        rank = [1 for _ in range(len(s))]
        
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
        
        for x, y in pairs:
            union(x,y)
        
        count = defaultdict(list)
        
        for i in range(len(s)):
            count[find(i)].append(i)
        
        
        for i in count:
            a = [s[j] for j in count[i]]
            a.sort()
            
            for j in range(len(a)):
                s[count[i][j]] = a[j]
        
        return ''.join(s)
        
        
            