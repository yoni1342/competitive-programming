class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda el: el[0])
        arr = []
        start,end = intervals[0][0],intervals[0][1]
        for i in intervals:
            if i[0]>end:
                arr.append([start,end])
                start,end = i[0],i[1]
            else:
                end = max(end,i[1])
        arr.append([start,end])
        return arr  