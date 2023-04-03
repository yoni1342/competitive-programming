class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        a = [True]*(n+1)
        
        for i in range(2, n):
            if a[i] == True:
                j = i*i
                while j < n:
                    a[j] = False
                    j+=i

                count += 1
        
        return count