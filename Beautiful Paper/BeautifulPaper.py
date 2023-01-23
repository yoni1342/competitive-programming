t = int(input())

for _ in range(t):
    rect1 = list(map(int, input().split()))
    rect2 = list(map(int, input().split()))

    c = set(rect1) & set(rect2)
    if not c:
        print("No")
        continue

    c = sorted(list(c))
    common = c[-1]

    for i,val in enumerate(rect1):
        if val == common:
            rect1.pop(i)
    for i,val in enumerate(rect2):
        if val == common:
            rect2.pop(i)

    if rect1[0]+rect2[0] == common:
        print("Yes")
        continue
    else:
        print("No")
        continue
        
