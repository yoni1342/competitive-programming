n = int(input())
graph = []
sources = []
sinks = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range(len(graph)):
    if len(set(graph[i])) == 1:
        sinks.append(i+1)


col  = list(zip(*graph))

for i in range(len(col)):
    if len(set(col[i])) == 1:
        sources.append(i+1)

print(len(sources),*sources)
print(len(sinks), *sinks)
