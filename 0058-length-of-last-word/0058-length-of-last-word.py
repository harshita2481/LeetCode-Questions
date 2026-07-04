class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s[::-1]
        i=0
        count=0
        while i<len(word):
            if word[i]==" " and count==0:
                i+=1
            elif word[i]!=" ":
                count+=1
                i+=1
            else:
                break
        return count