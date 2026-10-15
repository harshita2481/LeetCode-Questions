class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        chars=set()
        maxi=0
        while r<len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi
        