tt = int(input())

while tt:
    tt-=1
    n,m,k = list(map(int, input().split()))
    word1 = input()
    word2 = input()


    word1 = sorted(word1)
    word2 = sorted(word2)
    ans = ""
    while word2 and word1:
        c = 0
        if word1>word2:
            while word1<word2 and c<k:
                ans+=word1.pop(0)
                c+=1
            ans+=word2.pop(0)
        else:
            while word1>word2 and c<k:
                ans+=word2.pop(0)
                c+=1
            ans+=word1.pop(0)