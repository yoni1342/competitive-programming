class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in range(len(s)):
            if stack:
                if stack[-1][0] == s[i]:
                    stack[-1][1]+=1
                else:
                    stack.append([s[i], 1])
                
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i],1])
        
        
        return ''.join([x * i for x, i in stack])
    