class Tri:
    def __init__(self):
        self.kids = {}
        self.count = 0

class Solution:
    def __init__(self):
        self.root = Tri()
    def add(self,word):
        node =  self.root
        for char in word:
            if char  not in node.kids:
                node.kids[char] = Tri()
            node = node.kids[char]
            node.count += 1
    def search(self, word):
        ans = 0
        node = self.root
        for char in word:
            node = node.kids[char]
            ans += node.count
        return ans

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        for word in words:
            self.add(word)
        for word in words:
            ans.append(self.search(word))
            
        return ans


        