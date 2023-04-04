class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b,a%b)
    
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        
        return self.gcd(min_,max_)