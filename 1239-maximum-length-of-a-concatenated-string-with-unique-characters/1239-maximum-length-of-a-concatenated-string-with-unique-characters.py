class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        
        def back(idx, path):
            nonlocal ans
            ans = max(ans, len(path))
            
            if idx >= len(arr):
                return 
            
            for i in range(idx, len(arr)):
                
                j = 0
                flag = True
                unique = set()                
                while j < len(arr[i]):
                    if arr[i][j] in path or arr[i][j] in unique :
                        flag = False
                        break
                    unique.add(arr[i][j])
                    j+=1
                    
                if flag:
                    path.update(*arr[i])
                    back(i+1, path)
                    
                    for char in arr[i]:
                        path.remove(char)
                        
        back(0, set())
        return ans
            
            