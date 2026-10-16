class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def rt(g):
            odds=0
            l=0
            r=0
            count=0
            while r<len(nums):
                if nums[r]%2==1:
                    odds+=1
                while odds>g:
                    if nums[l]%2==1:
                        odds-=1
                    l+=1
                count+=r-l+1
                r+=1
            return count
        return rt(k)-rt(k-1)
        