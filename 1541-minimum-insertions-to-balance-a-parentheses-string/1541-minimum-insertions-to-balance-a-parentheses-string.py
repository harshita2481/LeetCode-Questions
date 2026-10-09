class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        ans=""
        count=0
        for i in s:
            if i=="(":
                if ans==")" and stack:
                    count+=1
                    stack.pop()
                    ans=""
                elif ans==")" and not stack:
                    count+=2
                    ans=""
                stack.append("(")
            elif i==")":
                if ans==")":
                    if stack:
                        stack.pop()
                    else:
                        count+=1
                    ans=""
                else:
                    ans=")"
        if ans==")" and stack:
            count+=1
            stack.pop()
        elif ans==")" and not stack:
            count+=2
        count+=2*len(stack)
        return count