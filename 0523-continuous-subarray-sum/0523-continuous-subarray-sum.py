class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        Hash = defaultdict(int)
        Hash[0] =  0
        runningSum = 0
        
        for i,val in enumerate(nums):
            runningSum+=val

            if runningSum%k in Hash:
                if i-Hash[runningSum%k]+1>=2:
                    return True
            else:
                Hash[runningSum%k] = i+1
        
        return False