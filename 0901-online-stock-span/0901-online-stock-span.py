class StockSpanner:

    def __init__(self):
        # store the days 
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append((price, 1))
        span = 0
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)