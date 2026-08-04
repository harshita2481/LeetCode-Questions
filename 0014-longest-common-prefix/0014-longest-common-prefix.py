class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        temp=strs[0]
        for i in range(1,len(strs)):
            ans=[]
            for j in range(min(len(temp),len(strs[i]))):
                if temp[j]==strs[i][j]:
                    ans.append(temp[j])
                else:
                    break
            temp="".join(ans)
        return "".join(ans)

        
            
        
            
