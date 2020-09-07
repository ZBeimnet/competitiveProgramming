class StockSpanner:

    def __init__(self):
        self.stock_prices = []

    def next(self, price: int) -> int:
        current_span = 1

        while self.stock_prices and self.stock_prices[-1][0] <= price:
            current_span += self.stock_prices.pop()[1]
        self.stock_prices.append((price, current_span))

        return current_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)