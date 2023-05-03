class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        ans.append(set(nums1).difference(nums2))
        ans.append(set(nums2).difference(nums1))        
        
        return ans