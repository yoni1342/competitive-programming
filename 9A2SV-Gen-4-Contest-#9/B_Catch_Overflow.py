import bisect
from functools import reduce
import operator

n = int(input())

stack = []
ans = 0

for _ in range(n):
    opp = list(input().split())
    
    if opp[0] == "for":
        stack.append(int(opp[1]))
    elif opp[0] == "end":
        stack.pop()
    else:
        pro = reduce(operator.mul, stack)

        if ans + pro > 2**32 -1:
            print("OVERFLOW!!!")
            break
        ans += pro

else:
    print(ans)


bisect.bisect_left()