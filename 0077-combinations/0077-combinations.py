class Solution:    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.arr = [num for num in range(1,n + 1)]
        self.n = n
        self.k = k
        self.ans = []
        self.backTracking(0,[])
        
        return self.ans
    
    def backTracking(self,idx,combination):
        
        
        if len(combination) == self.k:
            self.ans.append(combination[:])
            
            return 
        
        if idx >= self.n:
            return
        
        for i in range(idx,self.n):
            
            combination.append(self.arr[i])
            
            self.backTracking(i + 1, combination)
            
            combination.pop()
            