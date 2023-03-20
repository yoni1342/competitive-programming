tt = int(input())

code = set('codeforces')

while tt:
    a = input()
    if a in code:
        print("YES")
    else:
        print("NO")

    tt-=1