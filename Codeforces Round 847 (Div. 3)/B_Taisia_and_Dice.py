tt = int(input())

while tt:
    tt-=1
    n,s,r = list(map(int, input().split()))
    n = n-1
    
    taken = s-r

    stack = [taken for i in range(r//taken)]
    if r%taken>0:
        stack.append(r%taken)
    stack.sort(reverse=True)

    dif = n-len(stack)
    while dif!=0:
        temp = stack.pop()
        if temp>1:
            stack.append(temp-1)
            stack.append(1)
            dif-=1
        else:
            stack.append(temp)
            stack.sort()
    

    stack.append(s-r)
    print(*stack)