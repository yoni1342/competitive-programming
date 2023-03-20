from collections import defaultdict
tt = int(input())
while tt:
    tt-=1
    n = int(input())

    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    
    stack = []
    for i in range(n-1):
        Hash = defaultdict(int)
        for j in range(n):
            Hash[matrix[j][i]] += 1
            Hash = sorted(Hash.items(),key=lambda item:item[1])
            print(Hash)
            # if not stack:

            
    # print(*stack)