class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if max(coins) <= 0:
            return 0
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j-coin]
        return dp[amount]

# Comment:
# Using dynamic programming to solve this problem.
# Time complexity: O(n*amount), where n is the number of coins.
# Space complexity: O(amount), where n is the number of coins.

