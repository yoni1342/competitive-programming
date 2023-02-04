class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Hash = Counter(s1)
        
        p1 = 0
        p2 = len(s1)-1
        
        while p2<len(s2):
            s2Hash = Counter(s2[p1:p2+1])
            if s2Hash == s1Hash:
                return True
            p2+=1
            p1+=1
        return False