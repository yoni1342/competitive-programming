class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        
        for i in range(2**len(nums)):
            sub = []
            idx = 0
            while i:
                if i & 1 == 1:
                    sub.append(nums[idx])
                i>>=1
                idx+=1
            
            res = 0
            for i in sub:
                res |= i
            
            ans[res]+=1
        
        return ans[max(ans)]