class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
#         Insert all characters of s in to Hash Map
        sHash = Counter(s)
        
        for item in t:
            if item not in sHash:
                return item
            else:
                if sHash[item] == 0:
                    return item
                sHash[item] -= 1