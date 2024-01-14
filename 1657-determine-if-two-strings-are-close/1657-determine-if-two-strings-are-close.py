class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        print(w1, w2)
        
        for i in w1:
            if i not in w2:
                return False
        
        for i in w1.values():
            for j in w2:
                if w2[j] == i:
                    del w2[j]
                    break
        if len(w2)==0:
            return True
        else:
            return False
        