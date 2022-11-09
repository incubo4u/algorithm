class StockSpanner:
    def __init__(self):
        self.spans = []
        self.stack = []

    def next(self, price: int) -> int:
        span_lenght = 1
        if not self.stack:
            self.stack.append(price)
            self.spans.append(span_lenght)
        else:
            while self.stack and price >= self.stack[-1]:
                self.stack.pop()
                span_lenght += self.spans.pop()
            self.stack.append(price)
            self.spans.append(span_lenght)
        return self.spans[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
