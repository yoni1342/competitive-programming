class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = sorted([*nums1, *nums2])
        
        n = len(merged_arr)
        
        mid = n//2
        
        if n%2!=0:
            return float(merged_arr[mid])
        else:
            return (merged_arr[mid]+merged_arr[mid-1])/2