n = int(input())

a = list(map(int, input().split()))

p1 = 0

negative = 0
zeros = 0

count = []

while p1<n:
    if a[p1]<0:
        negative+=1
    if a[p1]==0:
        zeros+=1
           
    c = abs(a[p1]-1)
    count.append(c)
    p1+=1

totalOpe = sum(count)
if negative%2==0:
    totalOpe = totalOpe - negative*2
elif (negative-1) % 2==0:
    totalOpe = totalOpe - (negative-1)*2
    if zeros:
        totalOpe -= 2

print(totalOpe) 
