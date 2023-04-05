class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res =set()
        
        def prime(num):
            i = 2
            while i*i <= num:

                if num%i == 0:
                    res.add(i)
                    num = num//i
                else:
                    i+=1

            if num!=1:
                res.add(num)

        
        for i in nums:
            prime(i)
        
        return len(res)