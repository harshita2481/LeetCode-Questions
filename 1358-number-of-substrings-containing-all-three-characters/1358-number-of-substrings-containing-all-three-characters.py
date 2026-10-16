class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last=[-1,-1,-1]
        count=0
        for i in range(len(s)):
            if s[i]=="a":
                last[0]=i
            elif s[i]=="b":
                last[1]=i
            else:
                last[2]=i
            if last[0]!=-1 and last[1]!=-1 and last[2]!=-1:
                left=min(last)
                right=max(last)
                count+=left+1
        return count


        