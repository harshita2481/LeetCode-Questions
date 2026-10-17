class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def rt(g):
            l=0
            r=0
            count=0
            d=dict()
            while r<len(nums):
                d[nums[r]]=d.get(nums[r],0)+1
                while len(d)>g:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        del d[nums[l]]
                    l+=1
                count+=r-l+1
                r+=1
            return count
        return rt(k)-rt(k-1)
