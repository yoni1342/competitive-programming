tt = int(input())

pi = "314159265358979323846264338327"
while tt:
    tt-=1
    s = input()
    i = 0
    j = 0
    Flag = True
    while i < len(s) and j < len(pi) and j<31:
        if s[i] == pi[j]:
            i+=1
            j+=1
        else:
            print(i)
            Flag = False
            break
    if Flag:
        print(i)