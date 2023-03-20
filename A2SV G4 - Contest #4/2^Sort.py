tt = int(input())

pow2 = []

for i in range(50):
    pow2.append(2**i)

while tt:
    n, k = map(int, input().split())
    poww = pow2[:n]
    a = list(map(int, input().split()))
    ans = []
    res = []
    for i in range(n):
        ans.append(a[i]*poww[i])
    
    i=0
    while i<n-k:
        res.append(ans[i])
        i+=1
    while i<n:
        res.append(ans[i])
        i+=1
    res.sort()
    print(res[k-1])

    tt-=1