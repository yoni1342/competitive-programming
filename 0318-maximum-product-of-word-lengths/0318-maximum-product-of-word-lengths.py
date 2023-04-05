class Solution:
    def maxProduct(self, words: List[str]) -> int:
        Hash = {}
        ans = 0
        
        for i,val in enumerate(words):
            res = 0
            for j in set(val):
                mask = 1 << ord(j)-96
                res |= mask
            Hash[i] = res
        
        for i in Hash:
            for j in Hash:
                
                if Hash[i]&Hash[j] == 0:
                    ans = max(ans,len(words[i]) * len(words[j]))
        
        return ans