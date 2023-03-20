tt = int(input())

while tt:
    tt-=1
    n = int(input())
    s = list(input().split())

    s.sort(key=len, reverse=True)
    print(s)
    