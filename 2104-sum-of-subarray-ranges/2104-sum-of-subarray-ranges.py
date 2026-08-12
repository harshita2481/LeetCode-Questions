class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        def nse(nums):
            nser=[0]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]>=nums[i]:
                    stack.pop()
                nser[i]=stack[-1] if stack else n
                stack.append(i)
            return nser
        def nge(nums):
            nger=[0]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]<=nums[i]:
                    stack.pop()
                nger[i]=stack[-1] if stack else n
                stack.append(i)
            return nger
        def pse(nums):
            pser=[0]*n
            stack=[]
            for i in range(n):
                while stack and nums[stack[-1]]>nums[i]:
                    stack.pop()
                pser[i]=stack[-1] if stack else -1
                stack.append(i)
            return pser
        def pge(nums):
            pger=[0]*n
            stack=[]
            for i in range(n):
                while stack and nums[stack[-1]]<nums[i]:
                    stack.pop()
                pger[i]=stack[-1] if stack else -1
                stack.append(i)
            return pger
        def submin(nums):
            total=0
            nser=nse(nums)
            pser=pse(nums)
            for i in range(n):
                left=nser[i]-i
                right=i-pser[i]
                total+=left*right*nums[i]
            return total
        def submax(nums):
            total=0
            nger=nge(nums)
            pger=pge(nums)
            for i in range(n):
                left=nger[i]-i
                right=i-pger[i]
                total+=left*right*nums[i]
            return total
        return submax(nums)-submin(nums)
        
        

                