class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left=0
        right=0
        for i in s:
            if i=="(":
                left+=1
            elif i==")":
                if left:
                    left-=1
                else:
                    right+=1
        
        res=set()
        path=[]
        def dfs(i,left,right,count):
            if i==len(s):
                if left==0 and right==0 and count==0:
                    res.add("".join(path))
                return

            if s[i]=="(" and left>0:
                dfs(i+1,left-1,right,count)
            elif s[i]==")" and right>0:
                dfs(i+1,left,right-1,count)

            path.append(s[i])
            if s[i] not in "()":
                dfs(i+1,left,right,count)
            elif s[i]=="(":
                dfs(i+1,left,right,count+1)
            elif count>0:
                dfs(i+1,left,right,count-1)
            path.pop()
        dfs(0,left,right,0)
        return list(res)