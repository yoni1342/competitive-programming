tt = int(input())

while tt:
    tt-=1
    n = int(input())
    back = []
    front = []
    a = input()
    
    u1 = set()

    for i in range(n):
        u1.add(a[i])
        back.append(len(u1))
    
    u1 = set()

    for i in range(n-1, -1, -1):
        u1.add(a[i])
        front.append(len(u1))
    front = front[::-1]
    ans = -1
    for i in range(1,n):
        ans = max(ans, back[i-1] + front[i])

    print(ans) 

        