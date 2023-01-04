class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up=low=0
        
        for i in word:
            if i.isupper():
                up+=1
            else:
                low+=1
        return up==len(word) or low==len(word) or (up==1 and word[0].isupper())