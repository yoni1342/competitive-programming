class Solution:
    def decodeString(self, s: str) -> str:
        return self.rec(s)
    def rec(self, s):
        i = 0 
        res = ""
        while i<len(s):
            if s[i].isdigit():
                num = ""
                ss = ""
                count = 1
                
                while i<len(s) and s[i]!='[':
                    num+=s[i]
                    i+=1
                i+=1
                while i<len(s) and count:
                    if s[i]=='[':
                        count+=1
                    elif s[i] == "]":
                        count-=1
                    ss+=s[i]
                    i+=1
                i-=1
                res += self.rec(ss[:-1]) * int(num)
            else:
                res+=s[i]
            i+=1
        return res