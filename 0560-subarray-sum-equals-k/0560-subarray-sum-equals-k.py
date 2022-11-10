class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = tot = 0
        dic = {0 : 1}
        for i in nums:
            prefix_sum += i
            if prefix_sum - k in dic:
                tot += dic[prefix_sum - k]
            
            if prefix_sum not in dic:
                dic[prefix_sum] = 1
                continue
            dic[prefix_sum] += 1
        
        return tot