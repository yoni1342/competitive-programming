class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        return s == s[::-1]