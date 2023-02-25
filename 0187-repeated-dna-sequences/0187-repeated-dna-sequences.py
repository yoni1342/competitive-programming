class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        unique = set()
        
        if len(s)<=10:
            return []
        left = 0
        for right in range(9,len(s)):
            subArray = s[left:right+1]
            if subArray in unique:
                ans.add(subArray)
            unique.add(subArray)
            left+=1
        print(unique)

        return list(ans)