class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token in operations:
                A = stack.pop()
                B = stack.pop()
                if token == "+":
                    stack.append(B+A)
                elif token == "-":
                    stack.append(B-A)
                elif token == "*":
                    stack.append(B*A)
                else:
                    stack.append(int(B/A))
            else:
                stack.append(int(token))
        return stack.pop()
            