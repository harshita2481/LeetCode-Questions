class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        d=dict()
        r=0
        l=0
        fru=0
        maxi=0
        while r<len(fruits):
            d[fruits[r]]=d.get(fruits[r],0)+1
            fru+=1
            while len(d)>2:
                d[fruits[l]]-=1
                fru-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            maxi=max(fru,maxi)
            r+=1
        return maxi

        