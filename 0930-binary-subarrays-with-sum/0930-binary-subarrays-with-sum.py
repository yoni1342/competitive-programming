class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        Hash = defaultdict(int)
        Hash[0]+=1
        
        ans = 0
        runningSum = 0
        
        for i in nums:
            runningSum+=i
            
            if runningSum - goal in Hash:
                ans+=Hash[runningSum-goal]
            
            Hash[runningSum]+=1
            
        return ans