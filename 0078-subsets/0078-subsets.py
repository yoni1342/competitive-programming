class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        bit = 0
        for i in range(2**len(nums)):
            temp = i
            idx = 0
            res = []
            while temp:
                if temp & 1 == 1:
                    res.append(nums[idx])
                temp >>= 1
                idx+=1
            ans.append(res)
        
        return ans
                
                