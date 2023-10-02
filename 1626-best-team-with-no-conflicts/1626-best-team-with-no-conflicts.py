class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        t = sorted(zip(ages,scores))
        dp = [0] * len(ages)

        for i in range(len(t)):
            val = 0
            for j in range(i,-1, -1):
                if t[i][1] >= t[j][1]:
                    val = max(dp[j], val)
            dp[i] = val
            dp[i] += t[i][1] 
        
        return max(dp)