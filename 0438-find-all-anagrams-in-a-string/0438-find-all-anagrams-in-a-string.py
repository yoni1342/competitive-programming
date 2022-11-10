class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # "cbaebabacd"
#       "abc"
        if len(p)>len(s): 
            return []
        pHash, sHash = {}, {}
        for i in range(len(p)):
            pHash[p[i]] = 1+pHash.get(p[i], 0)
            sHash[s[i]] = 1+sHash.get(s[i], 0)
            
        res = [0] if pHash==sHash else [] 
        l = 0
        r = len(p)
        while r<len(s):
            sHash[s[r]] = 1+sHash.get(s[r], 0)
            sHash[s[l]] -= 1 
            
            if sHash[s[l]]==0:
                sHash.pop(s[l])
            l+=1
            
            if pHash==sHash:
                res.append(l)
            r+=1
        return res