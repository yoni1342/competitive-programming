class Solution:
    def self(sr,sc,image,color):
        self.sr = sr
        self.image = image
        self.color = color
        self.sc = sc
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.sr = sr
        self.image = image
        self.color = color
        self.sc = sc
        
        self.dfs(sr, sc, set())
        return image
    
    def inbound(self,row, col):
        return (0 <= row < len(self.image) and 0 <= col < len(self.image[0]))
    
    def dfs(self,row,col,visited):
        directions = [(1,0), (-1,0),(0,1),(0,-1)]
        visited.add((row,col))
        for rowi, coli in directions:
            nextrow = row + rowi
            nextcol = col + coli
            if self.inbound(nextrow, nextcol) and (nextrow, nextcol) not in visited and self.image[nextrow][nextcol] == self.image[self.sr][self.sc]:
                self.dfs(nextrow, nextcol,visited)
        
        self.image[row][col] = self.color