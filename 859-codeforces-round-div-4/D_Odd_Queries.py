t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # Compute the parity of the array
    array_parity = sum(a) % 2

    for i in range(q):
        l, r, k = map(int, input().split())
        length = r - l + 1

        # If the range contains even number of elements, then the parity of the range is always even
    
        # If k is odd and the range contains odd number of elements, then the parity of the range is odd
        if k % 2 == 1 and length % 2 == 1:
            print("YES")
        # If k is even and the range contains odd number of elements, then the parity of the range is even
        elif k % 2 == 0 and length % 2 == 1:
            print("NO")
        # If k is odd and the range contains even number of elements, then the parity of the range is even
        else:
            range_parity = (k * (length // 2)) % 2
            print("YES" if array_parity == range_parity else "NO")
