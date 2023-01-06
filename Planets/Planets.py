from collections import Counter
numTestCase = int(input())

for testCase in range(numTestCase):
    n, c = list(map(int, input().split()))
    planets = list(map(int, input().split()))
    Hash = Counter(planets)
    
    count = 0

    for i in Hash:
        if Hash[i]>=c:
            count+=c
        elif Hash[i]>=2 and Hash[i]<c:
            count+=Hash[i]
        else:
            count+=1
    
    print(count)
