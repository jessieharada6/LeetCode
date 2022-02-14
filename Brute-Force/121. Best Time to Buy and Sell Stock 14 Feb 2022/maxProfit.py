class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pMin = prices[0]
        pMax = prices[0]
        diff = pMax - pMin
        
        for i in range(1, len(prices)):
            if pMin > prices[i]:
                pMin = prices[i]
                pMax = prices[i]
            elif pMax < prices[i]:
                pMax = prices[i]
                diff = max(diff, pMax - pMin)
        
        return diff


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 1
        buy = 0
        diff = 0
        
        while sell < len(prices):
            diff = max(diff, prices[sell] - prices[buy])
            
            if prices[buy] > prices[sell]:
                buy += 1
            else:
                sell += 1
        
        
        return diff