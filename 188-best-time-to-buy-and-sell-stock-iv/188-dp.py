class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        dp = [[0]*(1 + 2*k) for _ in range(len(prices))]
        for i in range(1 + 2*k):
            if i % 2 == 1:
                dp[0][i] = - prices[0]
            else:
                dp[0][i] = 0
                
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            for j in range(1, 1 + 2*k):
                if j % 2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i]) 
        
        return dp[len(prices) - 1][2*k]

# Comment:
# Similar to 123-best-time-to-buy-and-sell-stock-iii
# We use a 2D array to store the maximum profit at each day, with 2*k+1 states:
# 0: no stock, no transaction
# 1: have stock, no transaction
# 2: no stock, one transaction
# ...
# n: if n is odd, then it means we have a stock in hand, and we have n//2 transactions
#     if n is even, then it means we don't have a stock in hand, and we have n//2 transactions
# 2*k: no stock, k transactions

# Time complexity: O(n*k)
# Space complexity: O(n*k)