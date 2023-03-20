t = int(input())

for i in range(t):
    ans = []
    n = int(input())
    nums = list(map(int, input().split()))
    sortedNums = sorted(nums)

    for num in nums:
        if num == sortedNums[-1]:
            ans.append(num - sortedNums[-2])
        else:
            ans.append(num - sortedNums[-1])
    answer = " ".join([str(i) for i in ans])
    print(answer)