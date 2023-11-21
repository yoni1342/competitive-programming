class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            if len(stack)!=0:
                if i == '}' and stack.pop()!="{":
                    return False
                if i == "]" and stack.pop()!='[':
                    return False
                if i == ")" and stack.pop()!= '(':
                    return False
            else:
                return False
        if len(stack)!=0:
            return False
        return True