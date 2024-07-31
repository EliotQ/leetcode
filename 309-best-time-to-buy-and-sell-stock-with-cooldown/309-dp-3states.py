class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0] * 3 for _ in range(len(prices))]
        # state 0: at the end of today, has stock
        # state 1: at the end of today, has no stock, today no sell
        # state 2: at the end of today, has no stock, today sell
        dp[0][0] = - prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + prices[i]
        
        return max(dp[len(prices) -1][1], dp[len(prices) -1][2])

# Comment:
# dp[i][0] means the cash at the end of today when we have a stock in hand
# dp[i][1] means the cash at the end of today when we don't have a stock in hand, today no sell
# dp[i][2] means the cash at the end of today when we don't have a stock in hand, today sell

# Transition function:
# end of today, has stock:
# 1. we have a stock in hand at the end of yesterday, then we don't sell it, so the cash we have is dp[i-1][0]
# 2. we don't have a stock in hand at the end of yesterday, then we buy a stock at the end of today, so the cash we have is dp[i-1][1] - prices[i]

# end of today, has no stock when start of today has no stock (no transaction today)
# dp[i][1] = max(dp[i-1][1], dp[i-1][2])

# end of today, has no stock when start of today has a stock (sell today)
# dp[i][2] = dp[i-1][0] + prices[i]

# Time complexity: O(n)
# Space complexity: O(n)