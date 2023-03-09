class Solution:
    def __init__(self):
        self.ans = []
        
    def splitString(self, s: str) -> bool:
        return self.backtrack(0,s)
    
    def backtrack(self, idx, s):
        if idx >= len(s):
            return len(self.ans) >= 2
        
        for i in range(idx, len(s)):
            val = int(s[idx : i+1])
            
            if len(self.ans) == 0 or val == self.ans[-1] - 1:
                self.ans.append(val)
                
                if self.backtrack(i+1, s):
                    return True
                
                self.ans.pop()        
        return False