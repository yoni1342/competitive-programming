from sys import stdout

# function to perform the query
def query(k, piles):
    stdout.write('? {} {}\n'.format(k, ' '.join(str(x) for x in piles)))
    stdout.flush()
    return int(input())

# loop through all test cases
t = int(input())
for _ in range(t):
    # read input
    n = int(input())
    piles = list(map(int, input().split()))

    # perform binary search to find the pile with the special stone
    l, r = 0, n-1
    while l < r:
        mid = (l+r) // 2
        total_weight = query(mid-l+1, range(l+1, mid+2))
        if total_weight % 2 == 0:
            r = mid
        else:
            l = mid+1

    # output the answer
    stdout.write('! {}\n'.format(l+1))
    stdout.flush()
