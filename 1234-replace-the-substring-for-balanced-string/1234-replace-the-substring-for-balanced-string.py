class Solution:
    def balancedString(self, s: str) -> int:
        Hash = defaultdict(int)
        ref = len(s)//4
        
        for i in s:
            Hash[i]+=1
        refHash = defaultdict(int)
        
        ans = float('inf')
        for i in Hash:
            rem = Hash[i]-ref
            if rem>0:
                refHash[i] = rem
        Map = defaultdict(int)
        
        left =0 
        count = 0
        for right in range(len(s)):
            if s[right] in refHash:
                Map[s[right]]+=1
            
                if refHash[s[right]]==Map[s[right]]:
                    count+=1
            
            while count and count == len(refHash):
                # update ans
                ans = min(ans,right - left + 1)
                
                if  s[left] in refHash:
                    Map[s[left]]-=1
                    
                    # update the count
                    if Map[s[left]]<refHash[s[left]]:
                        count-=1     
                    if Map[s[left]]==0:
                        del Map[s[left]]
                    
                left+=1
        
        return 0 if ans == float('inf') else ans