class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        stack=[]
        for i in range(2*len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i%len(nums)]:
                stack.pop()
            if i<len(nums):
                if not stack:
                    ans[i%len(nums)]=-1
                else:
                    ans[i%len(nums)]=stack[-1]
            stack.append(nums[i%len(nums)])
        return ans