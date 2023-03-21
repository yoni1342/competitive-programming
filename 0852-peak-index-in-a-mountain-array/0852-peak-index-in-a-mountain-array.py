class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = -1
        r = len(arr)
        
        while l+1<r:
            mid = (l+r)//2
            
            if arr[mid+1] < arr[mid] > arr[mid-1]:
                return mid
            
            elif arr[mid+1]<arr[mid]<arr[mid-1]:
                r = mid
            
            else:
                l = mid
        
        