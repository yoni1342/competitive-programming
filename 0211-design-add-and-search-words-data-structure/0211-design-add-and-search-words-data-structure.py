class TrieNode:

    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.isEOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("*")
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
            node = node.kids[char]
        node.isEOW = True
        

    def search(self, word: str) -> bool:
        return self.searchSubString(word,self.root)

    def searchSubString(self,word,root):
        node = root

        for index,char in enumerate(word):
            if char == ".":
                found = False
                for kid in node.kids.values():
                    found = found or self.searchSubString(word[index+1:],kid)
        
                return found
                    
            elif char not in node.kids:
                return False
            else:
                node = node.kids[char]
        
        return node.isEOW
