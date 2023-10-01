class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
        memo = {}
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i,j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i,j)] = dp(i+1, j+1) + 1
            
            else:
                memo[(i,j)] = max(dp(i+1, j), dp(i, j+1))
            
            return memo[(i,j)]
        
        return dp(0, 0)