class Solution:
    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            gcd = nums[i]
            if gcd == k:
                count+=1
            
            for j in range(i+1, len(nums)):
                gcd = self.gcd(gcd, nums[j])
                
                if gcd == k:
                    count+=1
                if gcd < k:
                    break
        
        return count