class Solution:
    def printVertically(self, s: str) -> List[str]:
        vertical = list(zip_longest(*s.split(' '), fillvalue = " "))
        s = []
        for i in vertical:
            s.append(''.join(list(i)).rstrip())
        return s