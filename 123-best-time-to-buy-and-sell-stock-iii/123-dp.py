class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0, 0, 0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        dp[0][2] = 0
        dp[0][3] = - prices[0]
        dp[0][4] = 0

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        
        return dp[len(prices) - 1][4]

# Comment:
# This solution uses dynamic programming to find the maximum profit from buying and selling stocks.
# We use a 2D array to store the maximum profit at each day, with 5 states:
# 0: no stock, no transaction
# 1: have stock, no transaction
# 2: no stock, one transaction
# 3: have stock, one transaction
# 4: no stock, two transactions

# The transition function is:
# On day i, we have 5 choices:
# 1. We have no stock, no transaction, then the profit is the same as the previous day.
# 2. We have a stock, no transaction, then we have two choices:
#    a. We have a stock on day i-1, then the cash we have is the same as the previous day.
#    b. We don't have a stock on day i-1, then we buy a stock on day i, so the cash we have is dp[i-1][0] - prices[i].
#    So dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]).
# 3. We have no stock, one transaction, then we have two choices:
#    a. We don't have a stock and have one transaction on day i-1, then the cash we have is the same as the previous day.
#    b. We have a stock and no transaction on day i-1, then we sell the stock on day i, so the cash we have is dp[i-1][1] + prices[i].
#    So dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i]).
# 4. We have a stock, one transaction, then we have two choices:
#    a. We have a stock and have one transaction on day i-1, then the cash we have is the same as the previous day.
#    b. We don't have a stock and no transaction on day i-1, then we buy a stock on day i, so the cash we have is dp[i-1][2] - prices[i].
#    So dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i]).
# 5. We have no stock, two transactions, then we have two choices:
#    a. We don't have a stock and have two transactions on day i-1, then the cash we have is the same as the previous day.
#    b. We have a stock and one transaction on day i-1, then we sell the stock on day i, so the cash we have is dp[i-1][3] + prices[i].
#    So dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]).

# one each day, for each state, either we keep the same state or we change to another state, so we use max to update the state.

# The profit we get is dp[len(prices) - 1][4], i.e. the cash we have at the last day when we don't have a stock and have two transactions.
# Time complexity: O(n)
# Space complexity: O(n)