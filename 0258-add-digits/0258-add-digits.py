class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        
        while len(s)!=1:
            sum_ = 0
            for i in s:
                sum_ += int(i)
            s = str(sum_)
        
        return int(s)