class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        for i in s:
            if i=="(":
                stack.append(score)
                score=0
            else:
                if score==0:
                    score=1
                else:
                    score*=2
                score+=stack.pop()
        return score