class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            count = 0
            one = 1
            
            while one <= i:
                if one & i != 0:
                    count+=1
                one = one << 1    
            ans.append(count) 
        return ans