class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        
        for word in words:
            dec = Counter(chars)
            for index,char in enumerate(word):
                if char not in dec:
                    break
                if dec[char] == 0:
                    break
                if index == len(word)-1:
                    res+=index+1
                dec[char]-=1
        return res