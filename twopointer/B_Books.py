n, t = list(map(int, input().split()))
books = list(map(int, input().split()))

res = 0
i=0

while i<n:
    if books[i]<t:
        Sum = books[i]
        j=i+1
        while j<n and Sum+books[j]<=t:
            Sum += books[j]
            j+=1
        res = max(res, j-i)
    
    i+=1
print(res)
