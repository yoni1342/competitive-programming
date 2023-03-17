class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(s):
            count = 1
            Sum = 0
            
            for i in nums:
                Sum+=i
                
                if Sum>s:
                    count+=1
                    Sum = i
                
            return count > k
        
        l = max(nums)-1
        r = sum(nums)+1
        
        while l+1<r:
            mid = (l+r)//2
            
            if check(mid):
                l = mid
            else:
                r = mid
        
        return r