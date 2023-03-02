class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        tHash = defaultdict(int)
        sHash = defaultdict(int)
        
        count = 0
        left = 0
        for i in t:
            tHash[i]+=1

        for right in range(len(s)):
            if s[right] in tHash:
                sHash[s[right]]+=1
            
                if tHash[s[right]]==sHash[s[right]]:
                    count+=1
            
            while count==len(tHash):
                if not res or len(res) > right-left+1:
                    res = s[left:right+1]
                if s[left] in tHash:
                    sHash[s[left]]-=1
                    if sHash[s[left]]<tHash[s[left]]:
                        count-=1
                left+=1
        
        return res