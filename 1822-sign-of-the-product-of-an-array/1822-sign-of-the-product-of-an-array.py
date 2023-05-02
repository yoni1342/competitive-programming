class Solution:
    def signFunc(self, a):
        if a<0:
            return -1
        elif a>0:
            return 1
        return 0
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        
        for i in nums:
            if self.signFunc(i)==0:
                return 0
            res  *= self.signFunc(i)
        
        return res