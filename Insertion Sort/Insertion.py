arr = [1,2,4,5,3]

def insertionSort1(n,arr):
    temp = arr[-1]
    i = n-1
    while i>0 and arr[i-1]>temp:
        arr[i] = arr[i-1]
        print(*arr)
        i-=1
    arr[i] = temp
    print(*arr)
    
insertionSort1(5,arr)