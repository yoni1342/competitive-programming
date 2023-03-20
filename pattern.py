n = int(input())

pattern = []
answer = ""

for i in range(n):
    s = input()
    pattern.append(s)

ziped = list(zip(*[list(i) for i in pattern]))

print(ziped)

for i in ziped:
    if len(set(i)) == 1:
        print(2)
        if "?" in i:
            answer+="x"
        else:
            answer+=''.join(set(i))
    elif len(set(i))>2:
        answer+="?"
    elif len(set(i))==2:
        if "?" in set(i):
            for j in i:
                if j != "?":
                    answer+=''.join(j)
                break
        else:
            answer+='?'
print(answer)