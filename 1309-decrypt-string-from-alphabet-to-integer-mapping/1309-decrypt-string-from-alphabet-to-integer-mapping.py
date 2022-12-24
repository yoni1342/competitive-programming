class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ""
        n = len(s)
        ptr = n-1

#        we'll loop from the end coz if we find "#" 
#        it will be easier to convers the next 2 numbers
        while ptr >= 0:
            if s[ptr] == '#':
                # if we find '#' we'll concatnate the next 2 digites 
                # and cast to int then get the ascii value by adding 96 
                asciiVal = int(s[ptr-2] + s[ptr-1])+96
                answer += chr(asciiVal)
                ptr-=2
            else:
                asciiVal = int(s[ptr])+96
                answer += chr(asciiVal)
            ptr-=1
        
#         the answer we'll be reverse coz we loop form back
        return answer[::-1]