class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0] * 4 for _ in range(len(prices))]
        # state 0: at the end of today, has stock
        # state 1: at the end of today, has no stock, yesterday no sell, today no sell
        # state 2: at the end of today, has no stock, yesterday no sell, today sell
        # state 3: at the end of today, has no stock, yesterday sell, today no sell(frozon)
        dp[0][0] = - prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i], dp[i-1][3] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        
        return max(dp[len(prices) - 1][1], dp[len(prices) - 1][2], dp[len(prices) - 1][3])

# Comment:
# dp[i][0] means the cash at the end of today when we have a stock in hand
# dp[i][1] means the cash at the end of today when we don't have a stock in hand, yesterday no sell, today no sell
# dp[i][2] means the cash at the end of today when we don't have a stock in hand, yesterday no sell, today sell
# dp[i][3] means the cash at the end of today when we don't have a stock in hand, yesterday sell, today no sell(frozon)

# Time complexity: O(n)
# Space complexity: O(n)