class Solution:
    def __init__(self):
        self.n = 0
        self.ans = ''
    def findKthBit(self, n: int, k: int) -> str:
        self.n = n
        self.rec('0', 1)
        return self.ans[k-1]
    
    def reverse(self, s):
        res = []
        for i in s:
            if i == "0":
                res.append("1")
            else:
                res.append("0")
        return ''.join(res)[::-1]
    
    def rec(self,s,count):
        # base case
        if count == self.n:
            self.ans = s
            return
        reve = self.reverse(s)
        return self.rec(s+'1'+reve, count+1)