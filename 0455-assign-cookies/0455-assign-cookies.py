class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        l=0
        r=0
        while l<len(g) and r<len(s):
            if g[l]<=s[r]:
                l+=1
                r+=1
            else:
                r+=1
        return l