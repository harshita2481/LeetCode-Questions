class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s
        r=list(int(i) for i in s)
        leng=len(r)
        while leng>k:
            i=0
            count=0
            ans=""
            new=0
            while i<len(r):
                if count==k:
                    ans+=str(new)
                    new=0
                    count=0
                new+=r[i]
                count+=1
                i+=1
            ans+=str(new)
            r=list(int(i) for i in ans)
            leng=len(r)
        return ans      