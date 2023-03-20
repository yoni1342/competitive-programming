tt = int(input())
Hash = {
    "Y":"e",
    "e":"s",
    "s": "Y"
}

while(tt):
    word = input()
    n = len(word)
    flag = "YES"
    if word[0] not in Hash:
        flag = "NO"
    for i in range(n-1):
        if word[i] not in Hash or Hash[word[i]] != word[i+1]:
            flag = "NO"
            break
    print(flag)
    tt-=1