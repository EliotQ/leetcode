class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[len(s)][len(t)] == len(s)

# Comment:
# In this solution, compared to 392-dp-find-length.py, we modify the transition function to dp[i][j] = dp[i][j-1] if s[i-1] != t[j-1].
# This is because we only need to delete the character in t,
# and we don't need to consider the case where we delete the character in s.

# Or in other words, we have the assumption that s is a subsequence of t,
# so we always have dp[i-1][j] <= dp[i][j-1] 
# so the transition function in 392-dp-find-length degenrates from 
#   dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if s[i-1] != t[j-1]
# to
#   dp[i][j] = dp[i][j-1] if s[i-1] != t[j-1]
# and this will work well if the assumption is correct.
# In case assumption is not correct, the degenerated transition function will also leads to dp[len(s)][len(t)] != len(s) and return False.
# So this solution is correct.
# but I'd prefer 392-dp-find-length.py because it's more general and can be used in other problems.