class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        
        ans = len(citations)
        for i in range(len(citations)):
            if i+1 > citations[i]:
                ans = i
                break
        return ans
                # 6,5,3,1,0
                # 3,1,1
                # 4,4,0,0
                # 9,7,4,1