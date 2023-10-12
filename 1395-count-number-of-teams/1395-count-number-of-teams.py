class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dec = [0]*len(rating)
        inc = [0]*len(rating)
        
        for i in range(len(rating)):
            for j in range(0, i):
                if rating[j]<rating[i]:
                    dec[i] += 1
                elif rating[j] > rating[i]:
                    inc[i] += 1
     
        ans = 0
        for i in range(len(rating)-1, -1, -1):
            for j in range(i-1, -1, -1):
                
                if rating[j] < rating[i]:
                    ans+=dec[j]
                if rating[j] > rating[i]:
                    ans+=inc[j]
        
        return ans
            