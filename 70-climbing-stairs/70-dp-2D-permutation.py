class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [[0]*(n+1) for _ in range(3)]
        dp[0][0] = 1
        
        for j in range(n+1):
            for i in range(1, 3):
                dp[i][j] = dp[i-1][j]
                if j >= i:
                    dp[i][j] += dp[-1][j-i]
        return dp[2][n]

# Comment:
# This problem is permutation.
# We first iterate over the knapsack capacity, then the items.

# Time complexity: O(n*3) = O(n), where n is the length of the array.
# Space complexity: O(n*3) = O(n), where n is the length of the array.