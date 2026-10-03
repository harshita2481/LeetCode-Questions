class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        meets=0
        ended=float('-inf')
        for i in intervals:
            if i[0]>=ended:
                meets+=1
                ended=i[1]
        return len(intervals)-meets