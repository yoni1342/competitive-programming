class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.rec('(', 1, 1)
        return self.ans
    
    def rec(self, s, topen, close):
        # base case
        if topen==self.n and close==0:
            self.ans.append(s)
            return
        
        if topen<self.n:
            self.rec(s+'(', topen+1, close+1)
        if topen==self.n and close:
            return self.rec(s+')', topen, close-1)
        if close:
            self.rec(s+')', topen, close-1)
            