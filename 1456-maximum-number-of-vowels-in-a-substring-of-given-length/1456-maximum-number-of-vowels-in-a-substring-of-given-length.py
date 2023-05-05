class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Hash = defaultdict(int)
        
        ans = 0
        count = 0 
        left = 0
        vowel = "aeiou"
        for right in range(len(s)):
            if s[right] in vowel:
                count+=1
            
            if right-left+1 == k:
                ans = max(ans,count)
                if s[left] in vowel:
                    count-=1
                left+=1
        
        return ans