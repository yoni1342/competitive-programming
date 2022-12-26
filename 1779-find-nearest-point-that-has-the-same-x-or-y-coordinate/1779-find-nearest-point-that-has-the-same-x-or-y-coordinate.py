class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = [] 
        ans = 0
        min_man = float('inf')
        for i, j in points:
            if i == x or j == y:
                manhattan = abs(x-i)+abs(y-j)
                min_man = min(manhattan, min_man)
        
        for k in range(len(points)):
            i, j = points[k][0], points[k][1]
            if (i == x or j == y) and abs(x-i)+abs(y-j) == min_man:
                return k
                
                        
        return -1
    