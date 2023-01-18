class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        Max = max(arr)
        
        for i in range(len(arr)-1):
            if arr[i]<Max:
                arr[i] = Max
            elif arr[i] == Max:
                Max = max(arr[i+1:len(arr)])
                arr[i] = Max
        arr[-1] = -1
        
        return arr