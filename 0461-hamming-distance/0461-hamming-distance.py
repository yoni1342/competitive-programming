class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        target = x^y
        ans = 0

        while target!=0:
            
            if target & 1 != 0:
                ans+=1
            
            target >>= 1
        
        return ans