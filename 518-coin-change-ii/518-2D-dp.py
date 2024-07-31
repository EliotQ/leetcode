class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[len(coins)][amount]

# Comment:
# Using dynamic programming to solve this problem.
# The transition function is:
# dp[i][j] += dp[i][j-coins[i-1]]
# This is because we are allowed to use the same coin multiple times.

# Time complexity: O(n*amount), where n is the number of coins.
# Space complexity: O(n*amount), where n is the number of coins.

# See 518-1D-dp.py for the solution using a 1D dp array.