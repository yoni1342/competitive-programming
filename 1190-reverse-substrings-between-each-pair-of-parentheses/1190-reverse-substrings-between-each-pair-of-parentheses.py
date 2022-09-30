class Solution:
    def reverseParentheses(self, s: str) -> str:
        order = list(s)
        stack = []
        temp = []
        for i in order:
            if i == ")":
                for j in range(len(stack)-1, -1,-1):
                    if stack[j]!='(':
                        temp.append(stack.pop())
                    else:
                        break
                temp.reverse()
                stack.pop()
                for k in range(len(temp)-1, -1, -1):
                    stack.append(temp.pop())
            else:
                stack.append(i)
        final = "".join(stack)
        return final