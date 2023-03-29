class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            count = 0
            bit = i
            while bit:
                if bit & 1 != 0:
                    bit = bit >> 1
                    count+=1
                else:
                    bit = bit >> 1
            ans.append(count)
            
        return ans