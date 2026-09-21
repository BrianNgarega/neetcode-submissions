class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''max_profit = 0

        min_price = float('inf') 

        for i in range (len(prices)):
            min_price = min(prices[i], min_price)
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
        return max_profit'''

        l,r = 0, 0 #left=buy right =sell
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit) 
            else:
                l = r
            r += 1
        return maxprofit   
