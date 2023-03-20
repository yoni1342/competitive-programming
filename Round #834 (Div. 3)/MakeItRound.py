tt = int(input())

for i in range(tt):
    n, m = map(int, input().split())
    temp = m
    while (temp*n)%10 != 0 and temp>n:
        temp-=1
    if (temp*n)%10 == 0:
        print(temp*n)
    else:
        print(m)      
    