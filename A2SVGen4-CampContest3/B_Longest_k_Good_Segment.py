n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = [0] * (10**6+1) 
count = 0 
left = 0 
len_ = 0 
l, r = 0, 0 
for right in range(n):
    freq[a[right]] += 1
    if freq[a[right]] == 1: 
        count += 1
    
    while count > k: 
        freq[a[left]] -= 1
        if freq[a[left]] == 0: 
            count -= 1
        left += 1
    
    if right - left + 1 > len_: 
        len_ = right - left + 1
        l, r = left, right

print(l+1, r+1)