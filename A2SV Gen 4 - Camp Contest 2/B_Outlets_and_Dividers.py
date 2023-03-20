def subarray_sum_greater_than_k(arr, k):
    n = len(arr)
    start = end = 0
    sum = arr[0]

    while end < n:
        if sum > k:
            print(arr[start:end+1])
            sum -= arr[start]
            start += 1
        else:
            end += 1
            if end < n:
                sum += arr[end]
    
    while sum > k and start < n:
        print(arr[start:end+1])
        sum -= arr[start]
        start += 1

arr = [2,2,2,2,2,2]
k = 3
subarray_sum_greater_than_k(arr, k)