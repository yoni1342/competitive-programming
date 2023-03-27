class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        arr = [num1 - num2 for num1,num2 in zip(nums1,nums2)]
        
        count = 0
        
        sorte = []
        
        for num in arr:
            
            count += bisect_right(sorte, num + diff)
            insort(sorte, num)
        
        return count