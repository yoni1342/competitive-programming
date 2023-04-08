from collections import defaultdict
n = int(input())
k = int(input())

graph = defaultdict(list)

for i in range(k):
    q = list(map(int, input().split()))
    if q[0] == 1:
        graph[q[1]].append(q[2])
        graph[q[2]].append(q[1])
    else:
        print(*graph[q[1]])
