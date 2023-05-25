class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        have = defaultdict(int)
        
        for i in bills:
            if i == 20:
                if have[5]==0 or (have[5] < 3 and have[10] == 0):
                    return False
            
                if have[10]:
                    have[10] -= 1
                    have[5] -= 1
                else:
                    have[5] -= 3
            elif i == 10:
                if have[5] == 0:
                    return False
                have[5]-=1
                have[10]+=1
            else:
                have[5] += 1
        
        return True
            