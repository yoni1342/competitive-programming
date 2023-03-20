n = int(input())

a = list(map(int, input().split()))
webe = 0
henok = 0

right = n-1
left = 0
turn = 0
while left < right:
    if a[left]>a[right] and turn==0:
        webe += a[left]
        left += 1
        turn = 1
    elif a[left]<a[right] and turn==0:
        webe += a[right]
        right -= 1
        turn = 1
    elif a[left]>a[right] and turn==1:
        henok += a[left]
        left += 1
        turn = 0
    elif a[left]<a[right] and turn==1:
        henok += a[right]
        right -= 1
        turn = 0
    elif a[left]==a[right] and turn==0:
        webe += a[left]
        left += 1
        turn = 1
    elif a[left]==a[right] and turn==1:
        henok += a[left]
        left += 1
        turn = 0
if left==right:
    if turn==0:
        webe += a[left]
    else:
        henok += a[left]
print(webe, henok)