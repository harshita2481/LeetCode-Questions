class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        score=0
        for i in s:
            if i=="(":
                stack.append("(")
                score+=1
            else:
                if not stack:
                    score+=1
                else:
                    stack.pop()
                    score-=1
        return abs(score)