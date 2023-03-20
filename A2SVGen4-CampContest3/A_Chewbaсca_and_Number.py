x = input()

a = [int(i) for i in x]

for i in range(len(a)):
    if a[i] > 4:
        a[i] = 9 - a[i]

if a[0] == 0:
    a[0] = 9

print(''.join(str(i) for i in a))
