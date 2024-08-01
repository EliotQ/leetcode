class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for j in range(1, len(t) + 1):
            dp[0][j] = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)] % (10 ** 9 + 7)
    
# Comment:
# In this solution, we use dynamic programming to solve this problem.
# The transition function is:
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1]
# dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1]

# In initialization, we consider how many ways to choose 0 characters from s to form empty string.
# There is only one way, which is to choose 0 characters. so dp[i][0] = 1 for all i.
# There is no way to choose non-empty string from empty string, so dp[0][j] = 0 for all j > 0.
# especially, dp[0][0] = 1, because there is only one way to choose 0 characters from empty string to form empty string.

# Time complexity: O(m*n)
# Space complexity: O(m*n)
