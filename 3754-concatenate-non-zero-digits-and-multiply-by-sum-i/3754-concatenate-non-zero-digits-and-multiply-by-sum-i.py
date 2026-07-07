class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""
        summ=0
        for i in str(n):
            if i=="0":
                continue
            x+=i
            summ+=int(i)
        return int(x)*summ if x else 0