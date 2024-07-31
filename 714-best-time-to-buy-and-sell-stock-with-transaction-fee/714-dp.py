class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = - prices[0] - fee
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[len(prices) - 1][1]

# class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = - prices[0] - fee
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[len(prices) - 1][1]

# Comment:
# Time complexity: O(n)
# Space complexity: O(n)

# We have 2 states: hold and not hold
# The transition function is:
# hold[i] = max(hold[i-1], not_hold[i-1] - prices[i] - fee)
# not_hold[i] = max(not_hold[i-1], hold[i-1] + prices[i])

