class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        memo = defaultdict(int)
        mod = (10**9)+7
        
        def rec(lenght):
            if lenght > high:
                return 0
            if lenght in memo:
                return memo[lenght]
            
            left = rec(lenght+zero)
            right = rec(lenght + one)
            
            if low <= lenght <= high:
                memo[lenght] = left+right+1
                return (left+right+1)%mod
            else:
                memo[lenght] = left+right
                return (left+right)%mod
        
        return rec(0)