class Solution:
    def checkValidString(self, s: str) -> bool:
        lo=0
        hi=0
        for i in s:
            if i=="(":
                lo+=1
                hi+=1
            elif i==")":
                lo-=1
                hi-=1
            else:
                lo-=1
                hi+=1
            lo=max(lo,0)
            if hi<0:
                return False
        return lo==0