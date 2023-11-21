class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        loopLenght = 0
        answer = ""
        
        while loopLenght < max(len(word1), len(word2)):
            if loopLenght < len(word1):
                answer+=word1[loopLenght]
            if loopLenght < len(word2):
                answer+=word2[loopLenght]
            loopLenght+=1
        return answer
        
        