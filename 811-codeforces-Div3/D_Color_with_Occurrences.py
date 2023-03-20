def find(a, b, t, s, match):
    global ans, ok
    Max = 0
    id = -1
    pos = -1
    for i in range(a, b + 1):
        for j in range(len(s)):
            str_j = s[j]
            if i + len(str_j) > len(t) or i + len(str_j) <= b:
                continue
            if t[i:i+len(str_j)] == str_j:
                if i + len(str_j) > Max:
                    Max = i + len(str_j)
                    id = j
                    pos = i
    if id == -1:
        ok = False
        return
    else:
        match.append((id, pos))
        ans += 1
        if Max == len(t):
            return
        else:
            find(max(pos + 1, b + 1), Max, t, s, match)


def solve():
    global ans, ok
    ans = 0
    ok = True
    t = input().strip()
    n = int(input().strip())
    s = []
    for i in range(n):
        s.append(input().strip())
    match = []
    find(0, 0, t, s, match)
    if not ok:
        print("-1")
    else:
        print(ans)
        for p in match:
            print(p[0]+1, p[1]+1)


if __name__ == "__main__":
    q = int(input().strip())
    for i in range(q):
        solve()
