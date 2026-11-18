class Solution:
    def minChanges(self, s: str) -> int:
        steps=0
        ones=0
        zeroes=0
        for i in range(len(s)):
            if s[i]=="1":
                ones+=1
                if zeroes%2==0:
                    zeroes=0
                    continue
                steps+=1
                zeroes+=1
                ones-=1
                
            else:
                zeroes+=1
                if ones%2==0:
                    ones=0
                    continue
                steps+=1
                ones+=1
                zeroes-=1
        return steps