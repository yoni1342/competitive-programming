class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#         [1,7,3,6,5,6]
#  prefix [0,1,8,11,17,22,28]
#  suffix  [0,6,11,17,20,27,28]
        prefix = [0] *(len(nums)+1)
        suffix =[0] *(len(nums)+1)
        ans = -1
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
            suffix[i+1] = suffix[i]+nums[len(nums)-1-i]
        for i in range(len(nums)):
            if prefix[i] == suffix[len(suffix)-2-i]:
                ans = i
                break
        return ans