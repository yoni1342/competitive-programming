class Solution:
    def countOrders(self, n: int) -> int:
        
        def fact(n):
            r = 1
            for i in range(1,n+1):
                r *= i 
            
            return r 


        return (fact(n*2)//(2**n))%(10**9+7)