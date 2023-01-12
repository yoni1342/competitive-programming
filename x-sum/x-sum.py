from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    maxsum = 0
    
    add = defaultdict(int)
    sub = defaultdict(int)

    for i in range(n):
        for j in range(m):
            add[i+j] += matrix[i][j]
            sub[i-j] += matrix[i][j]
    
    for i in range(n):
        for j in range(m):
            Sum = 0
            Sum += add[i+j]
            Sum += sub[i-j]            
            maxsum = max(maxsum, Sum - matrix[i][j])
    
    print(maxsum)
