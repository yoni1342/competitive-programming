class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            return 1/self.rec(abs(n), x)
        else:
            return self.rec(n,x)
    
    def rec(self, n, x):
        if n==1:
            return x
        
        if n%2==0:
            left = self.rec(n//2, x)
            return left*left
        else:
            left = self.rec(n//2, x)
            return left*left*x
        
        