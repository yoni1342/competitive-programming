class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0]        
        x2,y2 = coordinates[1]
        
        if x2-x1:
            slop = (y2 - y1)/(x2 - x1)
            intersection = y1-(slop*x1)

            res = True

            for x,y in coordinates:
                if (slop*x)+intersection != y:
                    res = False
                    break

            return res
        else:
            s = set()
            for x,y in coordinates:
                s.add(x)
            if len(s) == 1:
                return True
            else:
                return False
            