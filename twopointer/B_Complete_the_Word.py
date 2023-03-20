str = list(input())

if len(str)<26:
    print(-1)
    exit()

ref = set()
for i in range(26):
    ref.add(chr(65+i))
unique = set()

left = 0
right = 0

unknow = 0

flag = -1

while right<len(str):
    while str[right] in unique:
        if str[left] == '?':
            unknow-=1
        else:
            unique.remove(str[left])
            ref.add(str[left])
        left+=1
    
    if str[right] != '?':
        unique.add(str[right])
        ref.remove(str[right])
    else:
        unknow+=1

    right+=1

    if right-left == 26 and len(ref) == unknow:
        i = left
        while i<right:
            if str[i] == "?":
                str[i] = ref.pop()
            i+=1
        flag = ''.join(str)
        break

if flag!=-1:
    for i in range(len(str)):
        if str[i] == '?':
            str[i] = "A"
    flag  = ''.join(str)
print(flag)