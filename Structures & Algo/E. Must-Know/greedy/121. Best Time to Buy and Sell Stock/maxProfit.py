class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_in = math.inf

        for x in prices:
            profit = max(profit, x - buy_in)  # 当天价格减去之前的买进价格
            buy_in = min(buy_in, x)           # 买进的股票价格

        return profit