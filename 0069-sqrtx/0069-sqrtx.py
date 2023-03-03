class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        
        while left<=right:
            mid = left+(right-left)//2
            
            if mid*mid<x:
                ans = mid
                left = mid+1
            elif mid*mid > x:
                right = mid-1
            else:
                ans = mid
                break
        
        return ans
        