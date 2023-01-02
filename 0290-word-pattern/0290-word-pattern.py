class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the string s 
        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s)))