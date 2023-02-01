class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def divs(prefix, s1, s2):
            for i in range(len(prefix), len(s1)+1,len(prefix)):
                if s1[i-len(prefix):i] != prefix:
                    return False
            if i<len(s1) and s1[i:] != prefix:
                return False
            for i in range(len(prefix), len(s2)+1, len(prefix)):
                if s2[i-len(prefix):i] != prefix:
                    return False
            if i <len(s2) and s2[i:] != prefix:
                    return False
            
            return True
        prefix = ""
        if len(str1)>len(str2):
            prefix = str2
        elif len(str1)<len(str2):
            prefix = str1
        else:
            return str1 if str1==str2 else "" 
        
        ans = ""
        for i in range(len(prefix)):
            if divs(prefix[0:i+1], str1, str2):
                ans = prefix[0:i+1]
        
        return ans