from collections import defaultdict
n,m = map(int,input())
a = []
col = defaultdict(list)
row = defaultdict(list)
for i in range(n):
    a.append(list(map(int,input())))
for i in range(n):
    for j in range(m):
        col[j].append(a[i][j])
        row[i].append(a[i][j])
for i in range(n):
    for j in range(m):
        if 