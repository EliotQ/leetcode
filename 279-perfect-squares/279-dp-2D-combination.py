class Solution:
    def numSquares(self, n: int) -> int:
        max_i = int(n**(1/2)) + 1
        dp = [[float('inf')]*(n+1) for _ in range(max_i+1)]

        for i in range(max_i+1):
            dp[i][0] = 0
        for i in range(max_i+1):
            for j in range(1, n+1):
                if j < i**2:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-i**2] + 1)
        return dp[max_i][n]

# Comment:
# This problem is combination, with repetition.
# We first iterate over the items, then the knapsack capacity.

# Time complexity: O(n*max_i) = O(n), where n is the length of the array.
# Space complexity: O(n*max_i) = O(n), where n is the length of the array.