class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack,count = [],0
        if len(num) == k:
            return "0"
        for i in num:
            while stack and i<stack[-1] and count<k:
                stack.pop()
                count+=1
            stack.append(i)
        while count<k:
            stack.pop()
            count+=1
        ans = int(''.join(stack))
        return str(ans)