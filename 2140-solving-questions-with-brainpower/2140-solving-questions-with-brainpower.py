class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = [0]*len(questions)
        
        def dfs(i):
            if i>=len(questions):
                return 0
            
            if memo[i]:
                return memo[i]
            
            memo[i] = max(
                dfs(i+1),
                questions[i][0] + dfs(i+1 + questions[i][1])
            )
            return memo[i]
        
        
        return dfs(0)
            