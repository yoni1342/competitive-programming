class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s)-1
        self.reverse(p1,p2,s)
        return s
    def reverse(self,p1, p2,s):
        if p1>=p2:
            return
        s[p1], s[p2] = s[p2],s[p1]
        self.reverse(p1+1, p2-1,s)
        
        