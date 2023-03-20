n, x, y = list(map(int,input().split()))

def check(mid):
    if mid<min(x,y):return False
    mid -= min(x,y)
    return ((mid/x)+(mid/y)+1)>=n

l =0 
r = min(x,y)*n

while r>l+1:
    mid = l+(r-l)//2

    if check(mid):
        r=mid
    else:
        l = mid

print(r)