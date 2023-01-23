t = int(input())

for _ in range(t):
    n = int(input())

    matrix = []

    for i in range(n):
        row = list(map(int, input()))
        matrix.append(row)
    
    left, right,top, buttom = 0, n-1, 0, n-1

    numOfOperations = 0
    while left<right:
        for i in range(right-left):
            count = 0
            count+=matrix[top][left+i]
            count+=matrix[top+i][right]
            count+=matrix[buttom][right-i]
            count+=matrix[buttom-i][left]

            if count==1 or count==3:
                numOfOperations+=1
            elif count==2:
                numOfOperations+=2
        
        left+=1
        right-=1
        top+=1
        buttom-=1
    
    print(numOfOperations)
