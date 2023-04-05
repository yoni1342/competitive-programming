class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
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

            primes = []
            for i in range(len(a)):
                if a[i]:
                    primes.append(i)
            return primes
        
        primes = sieve(right+1)
        
        ptr = 0
        while ptr<len(primes) and primes[ptr] < left:
            ptr+=1
        
        dif = float('inf')
        n1 =-1
        n2 = -1

        while ptr < (len(primes)-1):
            if primes[ptr+1]-primes[ptr] < dif:
                dif = primes[ptr+1]-primes[ptr]
                n1 = primes[ptr]
                n2 = primes[ptr+1]
            ptr+=1
            
        return([n1,n2])