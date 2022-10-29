class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexHash = {}
        # s = "ababcbac adefegdehijhklij"
        ans = []
        for i,c in enumerate(s):
            indexHash[c] = i
        size , end = 1,0 
        for i in range(len(s)):
            end = max(end, indexHash[s[i]])
            if(i==end):
                ans.append(size)
                size = 0
                end = 0
            size+=1
        return ans