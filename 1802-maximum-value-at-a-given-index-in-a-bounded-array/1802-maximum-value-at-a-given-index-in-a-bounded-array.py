class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        left = 0
        right = maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.isPossible(mid, index, n, maxSum):
                left = mid
            else:
                right = mid - 1
        return left + 1
    
    def isPossible(self, a: int, index: int, n: int, sum: int) -> bool:
        left = max(a - index, 0)
        result = (a + left) * (a - left + 1) // 2
        right = max(a - ((n - 1) - index), 0)
        result += (a + right) * (a - right + 1) // 2
        return (result - a <= sum)