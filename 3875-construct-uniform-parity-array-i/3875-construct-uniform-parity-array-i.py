class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        if not nums1:
            return False
        if len(nums1)==1:
            return True
        eve=0
        odd=0
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                eve+=1
            else:
                odd+=1
        

