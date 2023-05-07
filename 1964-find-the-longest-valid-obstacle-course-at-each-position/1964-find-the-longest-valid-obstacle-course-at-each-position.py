class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        mimo = [10**8]*(len(obstacles)+1)
        ans =  []
        
        for n in obstacles:
            i = bisect.bisect(mimo, n)
            ans.append(i+1)
            mimo[i] = n
        
        return ans