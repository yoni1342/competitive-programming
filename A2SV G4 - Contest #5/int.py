s = "4329203044422434555566"
fav = ['4329',"2030444","22344","22434555566"]

fav = set(fav)

left = 0
right = 0

ans = 0

while right<len(s):
    while s[left:right] not in fav:
        right+=1
    if right!=len(s) and s[left:right] in fav:
        ans += 1
        left = right

print(ans)