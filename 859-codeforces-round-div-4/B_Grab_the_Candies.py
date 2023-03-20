def can_reorder_bags(n, a):
    num_even = sum(1 for x in a if x % 2 == 0)
    num_odd = n - num_even
    
    
    if num_even > 0 and num_odd > 0 and num_even <= n and num_odd <= n and num_even <= n // 2:
        mihai_candies = sum(x for x in a if x % 2 == 0)
        bianca_candies = sum(x for x in a if x % 2 == 1)
        if mihai_candies > bianca_candies:
            return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(can_reorder_bags(n, a))
