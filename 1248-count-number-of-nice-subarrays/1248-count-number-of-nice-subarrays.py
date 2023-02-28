class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = [0]*len(nums)
        
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                prefix[i]=1
        
        prefix = list(accumulate(prefix))
        Hash = defaultdict(int)
        Hash[0]+=1
        ans = 0
        
        for i in prefix:
            if i-k in Hash:
                ans+=Hash[i-k]
            Hash[i]+=1
        
        return ans
                