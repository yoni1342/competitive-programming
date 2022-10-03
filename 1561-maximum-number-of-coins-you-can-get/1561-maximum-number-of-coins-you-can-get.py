class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        Bob = 0
        Me = len(piles)-2
        Alice = len(piles)-1
        ans = 0
        while Bob<Me:
            ans+=piles[Me]
            Bob+=1
            Me-=2
            Alice-=2
        return ans