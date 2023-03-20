w,h,n = list(   map(int, input().split()))

def check(x):
    if (x//w) * (x//h) >= n:
        return True
    else:
        return False

l = 0 
r = max(w,h)*n
while l < r-1:
    mid = l+(r-l)//2

    if check(mid):
        r = mid
    else:
        l = mid

print(r)