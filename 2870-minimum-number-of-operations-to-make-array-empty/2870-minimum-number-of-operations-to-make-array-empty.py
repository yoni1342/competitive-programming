class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        count = list(counter.values())
        memo = defaultdict(int)
        if 1 in count:
            return -1
        
        
        def dp(x):
            if x == 0:
                return 0
            if x < 0:
                return float("inf")
            
            if x in memo:
                return memo[x]
            else:
                memo[x] = min(dp(x-2), dp(x-3))+1
                return memo[x]
        
        ans = 0
        for i in count:
            ans+=dp(i)
            
        return ans