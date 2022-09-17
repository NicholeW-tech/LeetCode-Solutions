class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            r += 1
                    
        return max_profit
            
         
            