class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        summ=0
        for i in range(len(nums)):
            s=set()
            d=0
            for j in range(i,len(nums)):
                if nums[j] not in s:
                    d+=1
                    s.add(nums[j])
                summ+=d*d
        return summ
        
