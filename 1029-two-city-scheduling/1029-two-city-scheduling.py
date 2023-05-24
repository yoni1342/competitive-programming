class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = []
        
        for a,b in costs:
            cost.append((a-b, (a, b)))
        
        cost.sort()
        
        l = 0
        r = len(cost)-1
        ans = 0
        
        while l<r:
            ans+=cost[l][1][0]
            ans+= cost[r][1][1]
            
            l+=1
            r-=1
        
        return ans