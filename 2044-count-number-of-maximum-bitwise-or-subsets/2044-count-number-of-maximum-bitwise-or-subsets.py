class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = defaultdict(int)
        count[0]+=1
        
        for num in nums:
            keyval = list(count.items())
            
            for key, val in (keyval):
                count[ key | num] += val
        
        return count[max(count)]