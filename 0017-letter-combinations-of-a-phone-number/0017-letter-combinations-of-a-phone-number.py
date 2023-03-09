class Solution:
    def __init__(self):
        self.ans =[]
        self.size = 0
        self.digits = ""
    def letterCombinations(self, digits: str) -> List[str]:
        self.size = len(digits)
        self.digits = digits
        Hash = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y", "z"],
        }
        self.back(0,[],Hash)
        return self.ans
    
    def back(self, index, path, Hash):
        if len(path) >= self.size and len(path):
            self.ans.append(''.join(path))
            return
        if index >= self.size:
            return 
        for i in range(len(Hash[self.digits[index]])):
            path.append(Hash[self.digits[index]][i])
            self.back(index+1, path, Hash)
            path.pop()