class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > minval:
                maxprofit = max(maxprofit, prices[i] - minval)
            else:
                minval = prices[i]
    
        return  maxprofit
