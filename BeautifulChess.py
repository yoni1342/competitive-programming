from collections import Counter
t = int(input())
space = input()
for test in range(t):
    matrix = []

    for _ in range(8):
        row = list(input().strip())
        matrix.append(row)
    if test!=t-1:
        space = input()
    
    hashArr = []
    
    for i in matrix:
        count = Counter(i) 
        hashArr.append(count['#'])
    row = 0
    col = 0
    for i,val in enumerate(hashArr):
        if i!=0 and val == 1 and hashArr[i-1] == 2:
            row = i
            break
    for j in range(len(matrix[row])):
        if matrix[row][j] == '#':
            col = j
            break
    
    print(str(row+1) +" "+str(col+1))

