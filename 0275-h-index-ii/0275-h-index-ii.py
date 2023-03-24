class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        def check(i):
            if i+1 > citations[i]:
                return True
            else:
                return False
            
        l = -1
        r = len(citations)
        
        while l+1<r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid
        
        return r