class Solution:
    def reverseParentheses(self, s: str) -> str:
        order = list(s)
        stack = []
        secon = []
        for i in order:
            if i == ")":
                for j in range(len(stack)-1, -1,-1):
                    if stack[j]!='(':
                        secon.append(stack.pop())
                    else:
                        break
                secon.reverse()
                stack.pop()
                for k in range(len(secon)-1, -1, -1):
                    stack.append(secon.pop())
            else:
                stack.append(i)
        final = "".join(stack)
        return final