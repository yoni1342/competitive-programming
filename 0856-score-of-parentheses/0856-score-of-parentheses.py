class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        
        for i in s:
            if i == "(":
                stack.append("(")
            else:
                if stack[-1].isdigit():
                    temp = int(stack.pop())*2
                    stack.pop()
                    
                    if stack and stack[-1].isdigit():
                        stack.append(str(temp+int(stack.pop())))
                    else:
                        stack.append(str(temp))
                else:
                    stack.pop()
                    if stack and stack[-1].isdigit():
                        stack.append(str(int(stack.pop())+1))
                    else:
                        stack.append('1')                        
                        
        return sum(map(int,stack))