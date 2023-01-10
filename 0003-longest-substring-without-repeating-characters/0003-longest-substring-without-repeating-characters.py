class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        # count that counts the longest substring in the string
        count = 0
        
        # to check if the char are not repeated we use set
        unique = set()
        
        while right<len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[right])
            count = max(count, right-left+1)
            
            right+=1
        
        return count