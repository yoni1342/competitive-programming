t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sortedarr = sorted(arr)

    flag = "Yes"
    for i in range(n-1):
        if sortedarr[i+1] != sortedarr[i]+1:
            if sortedarr[i]!=sortedarr[i+1]:
                flag = "No"
                break
       
    print(flag)
