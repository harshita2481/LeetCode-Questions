class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxx=0
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
            elif s[i]==")":
                count-=1
            else:
                continue
            maxx=max(maxx,count)
        maxx=max(count,maxx)
        return maxx