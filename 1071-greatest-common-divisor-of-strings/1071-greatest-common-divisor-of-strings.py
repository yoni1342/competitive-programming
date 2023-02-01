class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        
        if str1+str2 == str2+str1:
            gcd = str1[:gcd(len(str1), len(str2))]
            return gcd
        else:
            return ""