class Solution:
    def candy(self, ratings: list[int]) -> int:
        summ=1
        i=1
        while i<len(ratings):
            if ratings[i]==ratings[i-1]:
                summ+=1
                i+=1
                continue
            peak=1
            while i<len(ratings) and ratings[i]>ratings[i-1]:
                peak+=1
                summ+=peak
                i+=1
            down=0
            while i<len(ratings) and ratings[i]<ratings[i-1]:
                down+=1
                summ+=down
                i+=1
            if down+1>peak:
                summ+=down-peak+1
        return summ
        