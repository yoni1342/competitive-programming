class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a = [0]*(len(s)+1)

        for i in shifts:
            if i[2]==1:
                a[i[0]]+=1
                a[i[1]+1]-=1
            else:
                a[i[0]]-=1
                a[i[1]+1]+=1
        
        sl = []
        cur_sum = 0
        for i in range(len(a)-1):
            cur_sum += a[i]
            
            char = (((ord(s[i]) + cur_sum) - 97) % 26) + 97
            sl.append(char)
        
        res =[chr(i) for i in sl]
        
        return ''.join(res)