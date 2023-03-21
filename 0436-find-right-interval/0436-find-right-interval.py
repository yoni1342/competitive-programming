class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        
        a = intervals[:]
        
        for i in range(len(a)):
            a[i].append(i)
        
        a.sort()
        
        def check(target):
            l = -1
            r = len(a)
            
            while l+1<r:
                mid = (l+r)//2
                
                if a[mid][0]>=target:
                    r = mid
                else:
                    l = mid
                    
            if r >= len(a):
                return -1
            
            return a[r][2]
        
        ans = []
        for i in intervals:
            ans.append(check(i[1]))
        
        return ans