def countingSort(arr):
    # Write your code here
    results = [0] * (100)
    for i in arr:
        results[i] += 1
    return results
