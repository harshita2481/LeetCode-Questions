class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def histarea(prefix):
            stack=[]
            area=0
            for i in range(len(prefix)):
                while stack and prefix[stack[-1]]>=prefix[i]:
                    nse=i
                    curr=prefix[stack.pop()]
                    pse=stack[-1] if stack else -1
                    area=max(area,curr*(nse-pse-1))
                stack.append(i)
            while stack:
                nse=len(prefix)
                curr=prefix[stack.pop()]
                pse=stack[-1] if stack else -1
                area=max(area,curr*(nse-pse-1))
            return area

        maxi=0
        rows=len(matrix)
        cols=len(matrix[0])
        prefix=[[0 for i in range(cols)] for i in range(rows)]
        for j in range(cols):
            summ=0
            for i in range(rows):
                summ+=int(matrix[i][j])
                if matrix[i][j]=="0":
                    summ=0
                prefix[i][j]=summ
        for i in range(rows):
            maxi=max(maxi,histarea(prefix[i]))
        return maxi
            
        