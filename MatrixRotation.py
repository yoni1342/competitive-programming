    tt = int(input())

for i in range(tt):
    matrix = []
    for i in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)
    top,left,right,buttom = 0,0,1,1
    Flag = "NO"
    for i in range(4):
        Flag = "NO"
        if matrix[top][left] < matrix[top][right] and matrix[top][left]<matrix[buttom][left] and matrix[buttom][left]<matrix[buttom][right] and matrix[top][right]<matrix[buttom][right]:
            Flag = "YES"
            break
        else:
            temp = matrix[top][left]
            matrix[top][left] = matrix[buttom][left]
            matrix[buttom][left] = matrix[buttom][right]
            matrix[buttom][right] = matrix[top][right]
            matrix[top][right] = temp
    
    print(Flag)
