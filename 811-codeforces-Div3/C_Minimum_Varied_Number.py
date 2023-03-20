tt = int(input())
while tt:
    tt -= 1

    s = int(input())
    ans = []

    def back(i, path):
        if path and sum(path) == s:
            ans.append(int(''.join(list(map(str, path)))))
        if i == 10:
            return

        for j in range(i,10):
            path.append(j)
            back(j+1,path)
            path.pop()
    
    back(1,[])
    print(min(ans))