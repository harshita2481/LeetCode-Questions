class StockSpanner:

    def __init__(self):
        self.spans=[]
    def next(self, price: int) -> int:
        days=1
        while self.spans and self.spans[-1][0]<=price:
            days+=self.spans.pop()[1]
        self.spans.append([price,days])
        return days
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)