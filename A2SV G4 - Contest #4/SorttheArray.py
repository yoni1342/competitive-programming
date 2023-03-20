n = int(input())
a = list(map(int, input().split()))

swap = []

i=0
while i < n-1:
    start = 0
    end = 0
    if a[i]>a[i+1]:
        start = i
        while a[i]>a[i+1]:
            i+=1
            if i==n-1:
                break
        # if a[i+1] and a[i+1]>a[]:
        end = i
        swap.append([start,end])
        while start<end:
            a[start],a[end] = a[end],a[start]
            start+=1
            end-=1
        if len(swap)>2:
            break
        else:
            i=0
            continue
    i+=1
if len(swap)==1:
    print("yes")
    print(swap[0][0]+1,swap[0][1]+1)
elif len(swap)==0:
    print("yes")
    print(1,1)
else:
    print("no")