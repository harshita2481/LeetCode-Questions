class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=dict()
        for i in t:
            d[i]=d.get(i,0)+1
        l=0
        r=0
        counter=0
        mini=float('inf')
        start=-1
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=-1
            elif d[s[r]]>0:
                counter+=1
                d[s[r]]-=1
            else:
                d[s[r]]-=1
            while counter==len(t):
                if r-l+1<mini:
                    mini=r-l+1
                    start=l
                d[s[l]]+=1
                if d[s[l]]>0:
                    counter-=1
                l+=1
            r+=1
        return s[start:start+mini] if start!=-1 else ""
        