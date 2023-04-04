class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        c = n&1
        n>>=1
        while n:
            if n&1 == c:
                return False
            c = n&1
            n>>=1
        return True