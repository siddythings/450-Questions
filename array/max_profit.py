class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left] :
                left = right
            elif (prices[right] - prices[left]) > profit:
                profit = prices[right] - prices[left]

        return profit
