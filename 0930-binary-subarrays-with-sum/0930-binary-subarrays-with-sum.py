class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def ret(g):   
            if g<0:
                return 0 
            summ=0
            l=0
            r=0
            count=0
            while r<len(nums):
                summ+=nums[r]
                while summ>g:
                    summ-=nums[l]
                    l+=1
                count+=r-l+1
                r+=1
            return count
        return ret(goal)-ret(goal-1)