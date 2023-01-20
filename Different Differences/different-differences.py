t = int(input())

while(t):
    a = []
    k,n = list(map(int, input().split()))
    dif = n-k
    i = 0
    c = 1
    while i<k and c<=n:
      if i<dif:
        a.append(c)
        c+=i+2
      else:
        a.append(c)
        c+=1
      i+=1
      dif-=i
    print(' '.join(map(str, a)))
    t-=1
