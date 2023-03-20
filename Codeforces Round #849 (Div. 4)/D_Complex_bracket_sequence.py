s = list(input())
n = len(s)
operations = []

for i in range(n//2):
    if s[i] == '(':
        operations.append(i+1)

for i in range(n//2, n):
    if s[i] == ')':
        operations.append(i+1)

print(1)
print(len(operations))
for i in operations:
    print(i, end=' ')
    