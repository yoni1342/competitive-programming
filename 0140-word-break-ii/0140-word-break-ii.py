class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        path = []
        wordDict = set(wordDict)
        
        def back(i):
            if i >= len(s):
                ans.append(' '.join(path))
                return
            
            for j in range(i, len(s)):
                
                temp = s[i:j+1]
                
                if temp in wordDict:
                    path.append(temp)
                    back(j+1)
                    path.pop()
            
        back(0)
        return ans