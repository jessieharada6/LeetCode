class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_loss = mx = 0
        
        for cost, gain in transactions:
            total_loss += max(cost - gain, 0)
            mx = max(mx, min(cost, gain))
        
        return total_loss + mx

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = gain = loss = 0
        for cost, cashback in transactions:
            if cost >= cashback:
                total_lose += max(cost - cashback, 0)
                gain = max(gain, cashback)
            else:
                loss = max(loss, cost)
        
        return total_lose + max(gain, loss)
            