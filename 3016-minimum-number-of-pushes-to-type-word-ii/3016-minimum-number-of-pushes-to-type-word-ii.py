class Solution:
    def minimumPushes(self, word: str) -> int:
        d=dict()
        for i in word:
            d[i]=d.get(i,0)+1
        pairs=sorted(d.items(),key=lambda x:x[1],reverse=True)
        i=0
        j=1
        pushes=0
        while i<len(pairs):
            if i>7:
                j=2
            if i>15:
                j=3
            if i>23:
                j=4
            pushes+=(j*pairs[i][1])
            i+=1
        return pushes
