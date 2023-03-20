tt = int(input())

while tt:
    tt-=1
    n = int(input())
    a = list(map(int, input().split()))
    s = list(input())

    flag = "YES"
    if len(s)!= len(a):
        print("NO")
        continue

    p=0
    Hash = {}
    while p < len(a):
        if a[p] not in Hash:
            Hash[a[p]] = s[p]
        else:
            if s[p]!= Hash[a[p]]:
                flag = "NO"
                break
        
        p+=1
    print(flag)
