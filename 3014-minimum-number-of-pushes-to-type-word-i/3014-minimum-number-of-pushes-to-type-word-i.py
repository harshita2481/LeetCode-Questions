class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        i=0
        j=1
        pushes=0
        while i<n:
            if i>7:
                j=2
            if i>15:
                j=3
            if i>23:
                j=4
            pushes+=j
            i+=1
        return pushes