class Solution:
    def numSquares(self, n: int) -> int:
        max_i = int(n ** (1/2))
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(max_i+1):
            for j in range(1, n+1):
                if j >= i**2:
                    dp[j] = min(dp[j], dp[j-i**2]+1)
        return dp[n]

# Comment:
# This problem is combination, with repetition.
# We first iterate over the items, then the knapsack capacity(from left to right).
