class Solution:
    def fib(self, n: int) -> int:
        a = [0,1]
        
        if n == 0:
            return 0
        elif n ==1:
            return 1
        
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        
        return a[n]