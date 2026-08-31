class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def nse(arr):
            stack=[]
            nser=[-1]*len(arr)
            for i in range(len(arr)-1,-1,-1):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                nser[i]=stack[-1] if stack else len(arr)
                stack.append(i)
            return nser
        def pse(arr):
            stack=[]
            pser=[-1]*len(arr)
            for i in range(len(arr)):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                pser[i]=stack[-1] if stack else -1
                stack.append(i)
            return pser
        nser=nse(heights)
        pser=pse(heights)
        area=0
        for i in range(len(heights)):
            curr=heights[i]*(nser[i]-pser[i]-1)
            area=max(area,curr)
        return area
