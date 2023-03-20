n = int(input())
a = list(map(int, input().split()))

swap = {

}
for i in range(len(a)):
    Min = i
    for j in range(i,len(a)):
        if a[j]<a[Min]:
            Min = j
    if Min!=i:
        a[i],a[Min] = a[Min],a[i]
        swap[a[i]] = a[Min]
    if len(swap)>2:
        break
if len(swap)==1:
    print("yes")
    for i in swap:
        print(i,swap[i])
elif len(swap)==0:
    print("yes")
    print(1,1)
else:
    print("no")