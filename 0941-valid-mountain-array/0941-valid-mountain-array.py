class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        flag = False
        sec = False
        while i<len(arr)-1 and arr[i]<arr[i+1]:
            sec = True
            i+=1
        
        while sec and i<len(arr)-1 and arr[i]>arr[i+1]:
            flag = True
            i+=1
        if i<len(arr)-1:
            return False
        
        return flag