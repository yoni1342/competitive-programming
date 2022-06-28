def countSwaps(a):
    # Write your code here
    count = 0
    n = len(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count = count+1
    
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")

a = [1,2,3]
countSwaps(a)