class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr = []
        
        i = 0
        while i*i<=c:
            sqr.append(i*i)
            if i*i == c:
                return True
            if (i*i)+(i*i) == c:
                return True
            i+=1
        
        p1 = 0
        p2 = len(sqr)-1
        
        while p1<p2:
            if sqr[p1]+sqr[p2] == c:
                return True
            elif sqr[p1]+sqr[p2]>c:
                p2-=1
            else:
                p1+=1
        
        return False