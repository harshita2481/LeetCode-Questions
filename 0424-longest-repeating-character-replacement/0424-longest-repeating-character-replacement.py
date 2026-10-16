class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=dict()
        l=0
        r=0
        maxi=0
        maxf=0
        while r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            maxf=max(maxf,d[s[r]])
            while ((r-l+1)-maxf)>k:
                d[s[l]]-=1
                maxf=max(maxf,d[s[l]])
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi
