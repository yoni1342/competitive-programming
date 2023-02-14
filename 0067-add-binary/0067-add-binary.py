class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b)<len(a):
            b ='0'*(len(a)-len(b))+b
        elif len(a)<len(b):
            a = '0'*(len(b)-len(a))+a
            
        ans = ""
        cur = "0"
        
        for i in range(-1,-len(a)-1, -1):
            x = a[i]
            y = b[i]
            
            Sum = x+y+cur
            Sum = ''.join(sorted(Sum))

            if Sum == "011":
                ans = '0'+ans
                cur = '1'
            elif Sum == '111':
                ans = '1'+ans
                cur = '1'
            elif Sum == '000':
                ans = '0'+ans
                cur = '0'
            else:
                ans = '1'+ans
                cur = '0'
        
        if cur == '1':
            ans = '1'+ans
        
        return ans
                