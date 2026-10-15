class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum=sum(cardPoints[:k])
        maxi=lsum
        rsum=0
        for i in range(len(cardPoints)-1,len(cardPoints)-1-k,-1):
            rsum+=cardPoints[i]
            lsum-=cardPoints[k-1]
            k-=1
            maxi=max(maxi,lsum+rsum)
        return maxi