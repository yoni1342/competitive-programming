class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False
        
class Solution:
    def __init__(self):
        self.Hash = defaultdict(list)
        self.root = TrieNode()
        
#     def insert(self, word, indx):
#         node = self.root
        
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.EOW = True
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        for i in range(len(products)):
            temp = ""
            for char in products[i]:
                temp+=char
                if len(self.Hash[temp])< 3:
                    self.Hash[temp].append(i)
        
        ans = []
        
        temp = ""
        for char in searchWord:
            temp+=char
            
            ans.append(list(map(lambda x : products[x], self.Hash[temp])))
        
        return ans