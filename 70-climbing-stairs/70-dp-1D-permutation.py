class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        dp = [0] * (n+1)
        dp[0] = 1

        for j in range(n+1):
            for i in range(1, 3):
                if j >= i:
                    dp[j] += dp[j-i]
        
        return dp[n]

# Comment:
# This problem is permutation.
# We first iterate over the knapsack capacity, then the items.
