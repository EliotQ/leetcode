class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')]*(amount + 1) for _ in range(len(coins)+1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i, coin in enumerate(coins, 1):
            for j in range(1, amount+1):
                if j < coin:
                    dp[i][j] = dp[i-1][j]
                if j >= coin:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coin]+1)
        
        if dp[len(coins)][amount] < float('inf'):
            return dp[len(coins)][amount]
        else:
            return -1

# Comment:
# This problem is combination, with repetition.
# We first iterate over the items, then the knapsack capacity.
