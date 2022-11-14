class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        unique = set()
        Long = 0
        while r<len(s):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            Long =max(Long, r-l+1)
            r+=1
        return Long
            