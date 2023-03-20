n = int(input())
line = []

for i in range(n):
    line.append(tuple(map(int, input().split())))
line.sort()

def isgood(x):
    res = []

    for i in range(len(line)):
        time = abs((x - line[i][0])/ line[i][1])

        res.append((time,i))

    Max = max(res)

    if line[Max[1]][0]>=x:
        return True
    return False

l = line[0][0]
r = line[-1][0]

for i in range(70):
    mid  = (l+r)/2

    if isgood(mid):
        l = mid
    else:
        r = mid


res = []

for i in range(len(line)):
    time = abs((l - line[i][0])/ line[i][1])

    res.append((time,i))
Max = max(res)
print(Max[0])