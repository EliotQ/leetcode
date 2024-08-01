class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        for i in range(1, len(s) + 1):
            dp[i] = dp[i-1]
            for j in range(0, i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] += 1
        return dp[len(s)]

# Comment:
# In this solution, we use dynamic programming to solve this problem.
# The transition function is:
# dp[i] = dp[i-1] + count of palindromic substrings ending at index i
# This is similar to two pointers solution, but we use dynamic programming to store the count of palindromic substrings ending at index i.

# Time complexity: O(n^3), because we need to check whether each substring is palindromic, and the slice operation takes O(n) time.
# Space complexity: O(n)

# This is somehow not strictly dp solution. It is more like a brute force solution.