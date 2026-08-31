class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        area=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                nse=i
                curr=heights[stack.pop()]
                pse=stack[-1] if stack else -1
                area=max(area,(curr*(nse-pse-1)))
            stack.append(i)
        while stack:
            nse=len(heights)
            curr=heights[stack.pop()]
            pse=stack[-1] if stack else -1
            area=max(area,curr*(nse-pse-1))
        return area


