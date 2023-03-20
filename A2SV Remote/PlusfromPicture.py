n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = list(input())
    matrix.append(row)
center = [0, 0]
for i in range(1,n-1):
    for j in range(1,m-1):
        if matrix[i][j] == "*" and matrix[i-1][j]=="*" and matrix[i+1][j]=="*" and matrix[i][j+1]=="*" and matrix[i][j-1]=="*":
            center[0] = i
            center[1] = j
            break

if center[0] == 0 and center[1] == 0:
    print("NO")
else:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "*":
                if i!=center[0] and j != center[1]:
                    print("No")
                    exit()
    print("YES")