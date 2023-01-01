class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        for i in range(len(spaces)):
            if  i==0:
                ans+=s[:spaces[i]]
                ans+=" "
            else:
                ans+=s[spaces[i-1]:spaces[i]]
                ans+=" "
        ans+=s[spaces[i]:len(s)]
        return ans