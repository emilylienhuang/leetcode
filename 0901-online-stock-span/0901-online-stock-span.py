class StockSpanner:

    def __init__(self):
        # store the days 
        self.stack = []
        self.temp_stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)

        count_leq = 0
        while self.stack and self.stack[-1] <= price:
            num = self.stack.pop()
            if num <= price:
                count_leq += 1
            self.temp_stack.append(num)
        
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())
        return count_leq

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)