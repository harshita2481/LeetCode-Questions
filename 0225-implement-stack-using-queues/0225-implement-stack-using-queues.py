class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]
        self.i=0

    def push(self, x: int) -> None:
        if self.q1==[]:
            self.q1.append(x)
            for i in self.q2:
                self.q1.append(i)
            self.q2=[]
        else:
            self.q2.append(x)
            for i in self.q1:
                self.q2.append(i)
            self.q1=[]

    def pop(self) -> int:
        if self.q1==[]:
            val=self.q2.pop(0)
        else:
            val=self.q1.pop(0)
        return val

    def top(self) -> int:
        if not self.q1:
            return self.q2[0]
        else:
            return self.q1[0]        

    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()