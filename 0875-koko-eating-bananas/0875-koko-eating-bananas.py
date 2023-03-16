class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(t):
            Sum = 0
            for i in piles:
                Sum+= math.ceil(i/t)
            
            if Sum<=h:
                return True
            return False
        
        l = 1
        r = max(piles)
        
        while l<r:
            mid = (l+r)//2
            
            if check(mid):
                r = mid 
            else:
                l = mid+1
        
        return l