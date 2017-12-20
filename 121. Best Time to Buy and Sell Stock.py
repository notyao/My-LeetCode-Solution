class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_diff = 0
        for i in range(1, len(prices)):
            max_diff = max(max_diff, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_diff
