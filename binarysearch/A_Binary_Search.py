n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
a.sort()
queries = list(map(int, input().split()))

for query in queries:
    low = 0
    high = len(a)-1
    flag = "NO"

    while low<=high:
        mid = low+(high-low)//2

        if a[mid] == query:
            flag = "YES"
            break
        elif a[mid]>query:
            high = mid-1
        else:
            low = mid+1
    
    print(flag)