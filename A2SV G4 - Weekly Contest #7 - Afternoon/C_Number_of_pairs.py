n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

a.sort()
b.sort()

p1=0
p2=0
ans = 0
while p1<n and p2<m:
    if abs(a[p1]-b[p2]) == 1 or abs(a[p1]-b[p2])==0:
        ans+=1
        p1+=1
        p2+=1
    elif a[p1]<b[p2]:
        p1+=1
    elif a[p1]>b[p2]:
        p2+=1

print(ans)