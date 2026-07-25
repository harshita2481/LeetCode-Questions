class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        total=0
        n=len(height)
        prefix=[height[0]]*n
        suffix=[height[-1]]*n
        for i in range(1,n-1):
            prefix[i]=max(prefix[i-1],height[i])
            suffix[n-i-1]=max(suffix[n-i],height[n-i-1])
        prefix[n-1]=max(prefix[n-2],height[n-1])
        suffix[0]=max(suffix[1],height[0])
        for i in range(n):
            total+=min(prefix[i],suffix[i])-height[i]
        return total
