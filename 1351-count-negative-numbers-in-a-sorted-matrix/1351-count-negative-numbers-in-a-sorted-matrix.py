class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        negatives = 0
        col = 0
        for row in range(n - 1, -1, -1):
            while col < m and grid[row][col] >= 0:
                col += 1
            negatives += m - col
        return negatives
