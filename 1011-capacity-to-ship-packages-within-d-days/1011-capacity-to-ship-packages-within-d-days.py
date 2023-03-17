class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(s):
            count = 1
            Sum = 0
            
            for i in weights:
                Sum+=i
                
                if Sum>s:
                    count += 1
                    Sum = i
            
            return count > days
        
        l = max(weights)-1
        r = sum(weights)+1
        
        while l + 1 < r:
            mid = (l+r)//2
            
            if check(mid):
                l = mid
            else:
                r = mid
        
        return r
        