class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opp = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i in opp:
                A = stack.pop()
                B = stack.pop()
                if i == "+":
                    stack.append(B+A)
                elif i == "-":
                    stack.append(B-A)
                elif i == "*":
                    stack.append(B*A)
                else:
                    stack.append(int(B/A))
            else:
                stack.append(int(i))
        return stack.pop()
            