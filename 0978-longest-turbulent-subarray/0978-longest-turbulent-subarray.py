class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        left = 0
        n=len(arr)
        
        for right in range(1,len(arr)):
            
            comp = self.cmp(arr[right], arr[right-1])
            
            if comp == 0:
                ans = max(ans,right-left)
                left = right
            
            elif right<n-1 and comp * self.cmp(arr[right], arr[right+1]) == 1:
                ans = max(ans,right-left+2)
            else:
                ans = max(ans,right-left+1)
                left = right
            ans = max(ans, right-left)
                
        return ans
        
    
    def cmp(self, x, y):
        if x == y:
            return 0
        elif x>y:
            return 1
        else:
            return -1