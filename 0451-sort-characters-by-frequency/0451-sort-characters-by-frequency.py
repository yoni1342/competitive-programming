class Solution:
    def frequencySort(self, s: str) -> str:
        Hash = Counter(s)
        x = Hash.most_common()
        ans = ""
        for i in range(len(x)):
            ans += x[i][0]*x[i][1]
        return ans