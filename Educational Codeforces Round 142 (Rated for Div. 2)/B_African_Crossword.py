from collections import defaultdict
n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(input()))

col = defaultdict(list)
row = defaultdict(list)

for i in range(n):
    for j in range(m):
        col[j].append(matrix[i][j])
        row[i].append(matrix[i][j])

ans = []

for i in range(n):
    for j in range(m):
        colCount = 0
        rowCount = 0
        for k in col[j]:

            if k == matrix[i][j]:
                colCount+=1
        for k in row[i]:
            if k == matrix[i][j]:
                rowCount+=1
        if colCount <= 1 and rowCount<=1:
            print(matrix[i][j], end="")