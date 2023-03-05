class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        unique = set()
        Hash = {}
        
        for i in range(len(s)):
            Hash[s[i]] = i
        
        
        for i, val in enumerate(s):
            
            if val not in unique:
                
                while stack and stack[-1]>val and Hash[stack[-1]]>i:
                    unique.remove(stack.pop())
                    
                stack.append(val)
                unique.add(val)
            
        return ''.join(stack)
                    