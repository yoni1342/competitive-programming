class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split(" ")
        for i in range(len(temp)-1, 0, -1):
            for j in range(i):
                if temp[j][-1]>temp[j+1][-1]:
                    temp[j+1],temp[j] = temp[j],temp[j+1]
        for i in range(len(temp)):
            x = temp[i].replace(temp[i][-1], "")
            temp[i] = x

        res = " ".join(temp)
        return res
            