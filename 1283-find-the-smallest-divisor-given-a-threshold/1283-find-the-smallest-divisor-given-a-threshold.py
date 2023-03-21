class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check(d):
            
            s = 0
            for i in nums:
                s += math.ceil(i/d)
            
            return s<=threshold
        
        l = 0
        r = sum(nums)
        
        while l+1<r:
            mid = (l+r)//2
            
            if check(mid):
                r = mid
            else:
                l = mid
        
        return r