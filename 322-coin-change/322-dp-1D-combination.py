from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i, coin in enumerate(coins, 1):
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1

# Test cases:
# [1,2,5], 11
s = Solution()
print(s.coinChange([1,2,5], 11)) # 3

# Comment:
# This problem is combination.
# We first iterate over the items, then the knapsack capacity(from left to right).