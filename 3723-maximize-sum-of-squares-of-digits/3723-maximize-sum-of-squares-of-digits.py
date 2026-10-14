class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:
        ans=""
        if summ>num*9:
            return ""
        for i in range(num):
            if summ<9 and summ>0:
                ans+=str(summ)
                summ=0
            else:
                ans+="9"
                summ-=9
            if summ==0 and len(ans)<num:
                ans+="0"*(num-len(ans))
                break
        return ans