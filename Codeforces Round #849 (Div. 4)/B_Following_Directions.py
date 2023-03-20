tt = int(input())

while tt:
    n = int(input())
    a = input()
    x = 0
    y = 0
    flag = "NO"
    for i in a:
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        if x==1 and y==1:
            flag = "YES"
            break
    print(flag)
    tt-=1