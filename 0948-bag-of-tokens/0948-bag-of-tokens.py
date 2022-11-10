class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r,ans = 0, len(tokens)-1,0
        
        while(l<=r):
            if power>=tokens[l]:
                power-=tokens[l]
                ans+=1
                l+=1
            elif power<tokens[l] and ans>0 and l!=r:
                ans-=1
                power+=tokens[r]
                r-=1
            else:
                l+=1
        return ans