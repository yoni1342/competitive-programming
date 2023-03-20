tt = int(input())
while tt:
    tt-=1

    n = int(input())
    a = list(input())
    i = len(a)-1
    ans = []

    while i>=0:
        if int(a[i]) == 0:
            num = ""
            for _ in range(2):
                i-=1
                num+=a[i]
            ans.append(chr(96+int(num[::-1])))
        else:
            ans.append(chr(96+int(a[i])))
        i-=1
    print(''.join(ans[::-1]))