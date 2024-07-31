class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = - prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        
        return dp[len(prices)-1][1]

# Comment:
# dp[i][0] means the cash at day i when we have a stock in hand
# dp[i][1] means the cash at day i when we don't have a stock in hand

# The transition function is:
# 1. we want to have a stock in hand at day i, then we have two choices:
#    a. we have a stock in hand at day i-1, then we don't sell it, so the cash we have is dp[i-1][0]
#    b. we don't have a stock in hand at day i-1, then we buy a stock at day i, so the cash we have is -prices[i]
#    so dp[i][0] = max(dp[i-1][0], -prices[i])
# 2. we don't want to have a stock in hand at day i, then we have two choices:
#    a. we don't have a stock in hand at day i-1, then we don't buy a stock at day i, so the cash we have is dp[i-1][1]
#    b. we have a stock in hand at day i-1, then we sell the stock at day i, so the cash we have is prices[i] + dp[i-1][0]
#    so dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

# The profit we get is dp[len(prices)-1][1] - 0, i.e. the cash we have at the last day when we don't have a stock in hand.  
# Time complexity: O(n)
# Space complexity: O(n)
