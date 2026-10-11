class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d=[]
        for i in range(len(nums1)):
            d.append(abs(nums1[i]-nums2[i]))
        k=k1+k2
        if k>=sum(d):
            return 0
        el=max(d)
        freq=[0]*(el+1)
        for x in d:
            freq[x]+=1
        count=0
        for i in range(el,0,-1):
            count+=freq[i]
            if count==0:
                continue
            if k>=count:
                k-=count
            else:
                total=(count-k)*i*i + k*(i-1)*(i-1)
                total+=sum(freq[u]*u*u for u in range(i))
                return total
        return 0
