n, m = map(int, input().split())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

p2 = 0 #a2
p1 = 0 #a1

ans = 0

while p2<m and p1<n:
    while p1<n and a2[p2] > a1[p1]:
        p1+=1
    while p2<m and a2[p2] < a1[p1]:
        p2+=1
    if a2[p2] == a1[p1]:
        p3 = p2
        while p3<m and a2[p3]==a2[p2]:
            p3+=1
        p4 = p1
        while p4<n and a1[p4]==a1[p1]:
            p4+=1
        
        ans += ((p4-p1)*(p3-p2))
    
    p2 = p3
    p1 = p4

print(ans)