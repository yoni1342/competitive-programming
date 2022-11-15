class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = []
        for i in tokens:
            if i == '+':
                fir = int(Stack.pop())
                sec = int(Stack.pop())
                Stack.append(fir+sec)
            elif i == '-':
                fir = int(Stack.pop())
                sec = int(Stack.pop())
                Stack.append(sec-fir)
            elif i == '*':
                fir = int(Stack.pop())
                sec = int(Stack.pop())
                Stack.append(sec*fir)
            elif i == '/' and Stack[-1]!=0:
                fir = int(Stack.pop())
                sec = int(Stack.pop())
                Stack.append(sec/fir)
            else:
                Stack.append(int(i))
        return int(Stack[0])
            