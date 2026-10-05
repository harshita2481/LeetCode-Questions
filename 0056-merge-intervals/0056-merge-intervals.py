class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res=[]
        new=intervals[0]
        for i in intervals:
            if i[0]<=new[1]:
                new[1]=max(new[1],i[1])
            else:
                res.append(new)
                new=i
        res.append(new)
        return res