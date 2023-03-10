class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.rec(n,k)
    
    def rec(self,n,k):
        if n == 1:
            return 0
        mid = (2**(n-1))//2
        
        if k > mid:
            return int(not (self.rec(n-1, k-mid)))
        else:
            return self.rec(n-1,k)
        