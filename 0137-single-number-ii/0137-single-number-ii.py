class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        negative = 0
        Hash = defaultdict(int)
        
        for i in nums:
            if i<0:
                negative +=1
                i = -i
            idx = 0
            while i:
                if i&1 == 1:
                    Hash[idx]+=1
                idx+=1
                i>>=1
        
        ans = 0
        
        for i in Hash:
            mask = (Hash[i] % 3) << i
            ans |= mask
        
        if negative % 3 != 0:
            return -ans
        
        return ans