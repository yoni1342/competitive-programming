class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Hash = defaultdict(int)
        

        left = 0
        ans = 0
        most_frq = 0
        
        for right in range(len(s)):
            Hash[s[right]]+=1
            most_frq = Hash[max(Hash, key=Hash.get)]
            
            if (right-left+1)-most_frq > k:
                Hash[s[left]]-=1
                left+=1
        
        return len(s)-left