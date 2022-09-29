for i in range(n-1,-1,-1):
    temp = arr[i]
    j=i-1
    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j-=1
        print(*arr)
    arr[j+1] = temp
print(*arr)