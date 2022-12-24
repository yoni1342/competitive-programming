class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        Hash = {}
        for index,char in enumerate(order):
            Hash[char] = index
            
        for wordPtr in range(len(words)-1):
            if not self.isSorted(words[wordPtr], words[wordPtr + 1], Hash):
                return False
        return True
            
            
    def isSorted(self, word1, word2, order):
        if word1 == word2:
            return True
        for charPtr in range(len(word1)):
            if order[word1[charPtr]] < order[word2[charPtr]]:
                return True 
                break
            elif order[word1[charPtr]] > order[word2[charPtr]]:
                return False
            elif charPtr == len(word2)-1:
                return False
        return True