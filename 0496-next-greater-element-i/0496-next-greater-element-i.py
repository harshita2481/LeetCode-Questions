class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=dict()
        stack=[]
        ans=[]
        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                result[nums2[i]]=-1
            else:
                while stack and nums2[i]>stack[-1]:
                    stack.pop()
                if stack:
                    result[nums2[i]]=stack[-1]
                else:
                    result[nums2[i]]=-1
            stack.append(nums2[i])
        for j in nums1:
            ans.append(result[j])
        return ans