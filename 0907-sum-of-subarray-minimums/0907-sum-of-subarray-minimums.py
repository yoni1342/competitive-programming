class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack  = []
        res = 0
        
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i
                
                count = (mid - left_boundary) * (right_boundary - mid)
                res += (count * arr[mid])
            
            stack.append(i)
        
        return res%(10**9+7)