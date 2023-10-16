class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = False 
        

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    
    def insert(self, word):
        cur_root = self.root 
        for ch in word:
            if ch not in cur_root.kids:
                cur_root.kids[ch] = TrieNode() 
            
            cur_root = cur_root.kids[ch]
            
        cur_root.end = True 
    
    def search(self,word):
        cur_root = self.root
        for ch in word:
            if ch not in cur_root.kids:
                return False 
            cur_root = cur_root.kids[ch]
            if not cur_root.end:
                return False 
        
        return cur_root.end 


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = ""
        for word in words:
            if trie.search(word):
                if len(word) > len(ans):
                    ans = word 
                elif len(word) == len(ans):
                    if word < ans:
                        ans = word
        
        return ans