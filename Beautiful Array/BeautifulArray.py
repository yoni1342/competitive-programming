from collections import defaultdict
n = int(input())

arr = list(map(int, input().split()))

Hash = defaultdict(int)

for i in arr:
    if i < 0:
        Hash['-ve'] += 1
    elif i>0:
        Hash['+ve'] += 1
    else:
        Hash['zero'] += 1

r1 = []
r2 = []
r3 = []

if Hash['+ve'] != 0:
    c = 0
    e = 0
    for num in arr:
        if num<0 and c==0:
            r1.append(num)
            c+=1
        elif num>0 and e==0:
            r2.append(num)
            e+=1
        else:
            r3.append(num)

else:
    c=0
    e=0
    for num in arr:
        if num<0 and c==0:
            r1.append(num)
            c+=1
        elif num<0 and e!=2:
            r2.append(num)
            e+=1
        else:
            r3.append(num)

a1 = str(len(r1))+' '+' '.join(map(str, r1))
a2 = str(len(r2))+' '+' '.join(map(str, r2))
a3 = str(len(r3))+' '+' '.join(map(str, r3))

print(a1)
print(a2)
print(a3)
