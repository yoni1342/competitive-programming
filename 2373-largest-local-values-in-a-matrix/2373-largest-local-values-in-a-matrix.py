class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)-2
        res = [[0]* N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                res[i][j] = max([grid[r][c] for r in range(i, i+3) for c in range(j, j+3)])

        return res