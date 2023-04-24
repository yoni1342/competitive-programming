class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final = max(nums)
        ref = set(nums)
        
        ans = []
        for i in range(1,len(nums)+1):
            if i not in ref:
                ans.append(i)
        
        return ans