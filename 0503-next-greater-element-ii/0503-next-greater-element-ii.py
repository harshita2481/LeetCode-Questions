class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        stack=[]
        for i in range(2*len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i%len(nums)]:
                stack.pop()
            if i<len(nums):
                if not stack:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
            stack.append(nums[i%len(nums)])
        return ans[::-1]