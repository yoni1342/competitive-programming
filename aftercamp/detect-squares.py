class DetectSquares:
    def __init__(self):
        self.ps = Counter()

    def add(self, point: List[int]) -> None:
        self.ps[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for x2, y2 in self.ps:
            if abs(x1-x2)==abs(y1-y2) and (x1!=x2 or y1!=y2):
                ans += self.ps[(x2, y2)]*self.ps[(x1, y2)]*self.ps[(x2, y1)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)