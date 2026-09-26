class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d=dict()
        for i in knowledge:
            d[i[0]]=i[1]
        ans=""
        k=""
        op=False
        for i in s:
            if i=="(":
                op=True
                continue
            elif i==")":
                if k in d:
                    ans+=d[k]
                else:
                    ans+="?"
                op=False
                k=""
                continue
            if op:
                k+=i
            else:
                ans+=i
        return ans