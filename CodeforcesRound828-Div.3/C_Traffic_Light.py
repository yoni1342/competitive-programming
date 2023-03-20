tt = int(input())
while tt:
    tt-=1
    temp = input().split()
    n = int(temp[0])
    cur = temp[1]
    a = list(input())

    res = 0
    

    if cur == 'g':
        print(0)
        continue


    left = 0
    right = 0
    while left<n:
        
        if a[left] == cur:
            if right<=left:
                right = left
                while a[right%n]!='g':
                    right+=1
                
            res = max(res, abs(right-left))
        left+=1
    
    print(res)