class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeroes=0
        maxi=0
        l=0
        r=0
        while r<len(nums):
            if nums[r]==0:
                zeroes+=1
            if zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi
