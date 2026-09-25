class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            if maxi<i:
                return False
            if i+nums[i]>maxi:
                maxi=i+nums[i]
        return True