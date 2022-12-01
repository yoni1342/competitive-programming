class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        s=s.lower()
        voewls = ['a','e','i','o','u']
        a = Counter(s[:mid])
        b = Counter(s[mid:])
        A = 0
        B = 0
        for i in voewls:
            if a[i]:
                A+=a[i]
            if b[i]:
                B+=b[i]
        if A==B:
            return True
        else:
            return False
        
        
        