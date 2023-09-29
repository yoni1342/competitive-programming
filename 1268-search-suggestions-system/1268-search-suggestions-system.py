class Solution:
    def __init__(self):
        self.Hash = defaultdict(list)
        
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