class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        ans = []
        for i in a:
            ans.append(i[::-1])
        
        return " ".join(ans)