class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr=[i*i for i in nums]
        arr.sort()
        summ=0
        for i in range(len(arr)-1,(len(arr)//2)-1,-1):
            summ+=arr[i]
        for i in range(len(arr)//2):
            summ-=arr[i]
        return summ