tt = int(input())

while tt:
    tt-=1
    n = int(input())
    a = []
    unique = set()
    for i in range(n):
        s = input()
        a.append(s)
        unique.add(s)
    
    ans = ''
    
    for str in a:
        flag = False
        for j in range(1,len(str)):
            first = str[:j]
            second = str[j:]
            if first in unique and second in unique:
                flag = True
                break
        if flag:
            ans+='1'
        else:
            ans+='0'
    print(ans)
            