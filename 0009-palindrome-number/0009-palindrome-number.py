class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=0
        n=x
        if n<0:
            return False
        while x!=0:
            c=c*10 + x%10
            x=x//10
        if c==n:
            return True
        else:
            return False
        