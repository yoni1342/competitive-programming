from collections import defaultdict
n = int(input())

graph = defaultdict(list)

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            graph[i+1].append(j+1)

for i in graph:
    print(len(graph[i]),*graph[i])
