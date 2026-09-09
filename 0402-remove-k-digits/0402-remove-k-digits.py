class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=1:
            return "0"
        stack=[]
        step=k
        for i in range(len(num)):
            while stack and num[i]<stack[-1] and step>0:
                stack.pop()
                step-=1
            stack.append(num[i])
        if step:
            stack=stack[:-step]
        result="".join(stack).lstrip("0") if len(stack)>1 else "".join(stack)
        return result if result else "0"


        