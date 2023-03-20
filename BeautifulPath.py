n, m = list(map(int, input().split()))

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# find S and T postion

tcord = []
scord = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            scord.append(i)
            scord.append(j)
        if matrix[i][j] == "T":
            tcord.append(i)
            tcord.append(j)

# Mark S
for i in range(scord[1], -1, -1):
    if matrix[scord[0]][i] == ".":
        matrix[scord[0]][i] = "S"
    elif matrix[scord[0]][i] == "T":
        print("Yes")
        exit()
    else:
        break


for i in range(scord[0], -1, -1):
    if matrix[scord[0]][i] == ".":
        matrix[scord[0]][i] = "S"
    elif matrix[scord[0]][i] == "T":
        print("Yes")
        exit()
    else:
        break


def mark(i, j, x, y, ch):
    newi = i+x
    newj = j+y

    if inbound(newi, newj) and matrix[newi][newj] == ".":
        matrix[newi][newj] = ch
        mark(newi, newj, x, y)
    return