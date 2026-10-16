class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        maxi=0
        d=dict()
        while r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            while len(d)==3:
                maxi+=len(s)-r
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            r+=1
        return maxi       