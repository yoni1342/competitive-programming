class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        a = [True]*(n)
        a[0] = False
        a[1] = False
        
        for i in range(2, int(math.sqrt(n))+1):
            if a[i] == True:
                j = i*i
                while j < n:
                    a[j] = False
                    j+=i

        count = 0
        for i in a:
            if i:
                count+=1
        
        return count