class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        Hash = defaultdict(int)
        ans = 0
        
        for num in nums:
            if k-num in Hash:
                ans+=1
                Hash[k-num]-=1
                
                if Hash[k-num] == 0:
                    del Hash[k-num]
            else:
                Hash[num]+=1
        
        return ans