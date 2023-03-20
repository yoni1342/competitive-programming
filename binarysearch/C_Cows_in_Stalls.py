n, k = list(map(int, input().split()))

a = list(map(int, input().split()))


def check(s):
    count = 1
    po = a[0]

    for i in a:
        if abs(po-i)>=s:
            count+=1
            po = i
    
    return count>=k

l = -1
r = a[-1]-a[0]+1

while l + 1 < r:
    mid = (l+r)//2

    if check(mid):
        l = mid
    else:
        r = mid

print(l)