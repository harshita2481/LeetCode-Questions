class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i]>=10:
                el=nums[i]
                total=0
                while el>0:
                    total+=el%10
                    el=el//10
                if i==total:
                    return i
            elif i==nums[i]:
                return i        
        return -1
