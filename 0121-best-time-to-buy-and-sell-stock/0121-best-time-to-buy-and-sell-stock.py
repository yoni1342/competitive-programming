class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        Max = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            Max= max(Max, prices[r]-prices[l])
            r+=1
        return Max