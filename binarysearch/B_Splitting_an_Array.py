n, k = list(map(int, input().split()))

a = list(map(int, input().split()))


def check(s):
    count = 1
    Sum = 0
    
    for i in a:
        Sum += i
        
        if Sum > s:
            count+=1
            Sum=i
    
    return count > k

l = max(a)-1
r = sum(a)+1

while l + 1 < r:
    mid = (l+r)//2

    if check(mid):
        l = mid
    else:
        r = mid

print(r)