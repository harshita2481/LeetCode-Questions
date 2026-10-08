class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        d=[]
        for i in intervals:
            d.append((i[0],"A"))
            d.append((i[1],"D"))
        d.sort()
        count=0
        maxi=0
        for i in d:
            if i[1]=="A":
                count+=1
                maxi=max(maxi,count)
            else:
                count-=1
        maxi=max(maxi,count)
        return maxi