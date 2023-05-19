class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(x):
            if x == parent[x]:
                return x
            r = find(parent[x])
            parent[x] = r
            return r
    
        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if rank[rep_x] > rank[rep_y]:
                    parent[rep_y] = rep_x
                    rank[rep_x] += rank[rep_y]
                else:
                    parent[rep_x] = rep_y
                    rank[rep_y] += rank[rep_x]

        

        for i in range(n):
            for j in range(i+1 ,n):
                if i != j:
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                        union(i ,j)
  
        for i in range(n):
            find(i)
            
        return n - len(set(parent))



            
            
        
        
            
