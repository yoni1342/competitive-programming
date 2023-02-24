class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = [1] + [0]*k
        ans = 0
        
        for num in nums:
            prefix = (prefix+num) % k
            ans += count[prefix]
            count[prefix] += 1
        
        return ans
                
                