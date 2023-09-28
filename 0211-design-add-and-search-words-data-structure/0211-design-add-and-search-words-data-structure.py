class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.EOW = True

    def search(self, word: str) -> bool:
        return self.searchSubString(word, self.root)

    def searchSubString(self, word, root):
        node = root
        
        for index, char in enumerate(word):
            if char == ".":
                found = False
                for i in node.children.values():
                    found = found or self.searchSubString(word[index+1:], i)
                return found
            
            elif char not in node.children:
                return False
            else:
                node = node.children[char]
            
        return node.EOW


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)