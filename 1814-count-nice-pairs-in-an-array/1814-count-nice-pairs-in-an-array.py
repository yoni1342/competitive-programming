class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] = int(str(nums[i])[::-1])-nums[i]
        
        temp = Counter(nums)
        ans = 0
        for i in temp:
            n = temp[i]
            ans+=(n*(n-1))//2
            
        return ans%(10**9 + 7)