class MyStack:

    def __init__(self):
        self.q=[]
        
    def push(self, x: int) -> None:
        self.q.append(x)
        for k in range(len(self.q)-1):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        val=self.q.pop(0)
        return val

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.q==[]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()