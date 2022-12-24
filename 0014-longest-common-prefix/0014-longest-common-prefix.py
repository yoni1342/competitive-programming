class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = min(strs, key=len)
        
        for i in range(len(answer)):
            for other in strs:
                if i<len(answer) and other[i] != answer[i]:
                    answer = answer[:i]
                    
        return answer