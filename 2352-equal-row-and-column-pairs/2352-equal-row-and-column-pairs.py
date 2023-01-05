class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpos = []
        for i in range(len(grid)):
            transposRow = []
            for j in range(len(grid[0])):
                transposRow.append(grid[j][i])
            transpos.append(transposRow)
        
        count = 0
        for i in grid:
            for j in transpos:
                if i==j:
                    count+=1
        
        return count