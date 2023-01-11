class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        
        for i in range(len(strs[0])):
            string = ""
            for j in range(len(strs)):
                string += strs[j][i]
            string = [i for i in string]
            sortstr = sorted(string)
            if string != sortstr:
                ans+=1
        return ans