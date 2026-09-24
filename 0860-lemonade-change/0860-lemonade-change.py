class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives=0
        tens=0
        twenties=0
        for i in range(len(bills)):
            if bills[i]==5:
                fives+=1
            elif bills[i]==10:
                tens+=1
                fives-=1
            else:
                twenties+=1
                if tens:
                    tens-=1
                    fives-=1
                else:
                    fives-=3
            if tens<0 or fives<0 or twenties<0:
                return False
        return True