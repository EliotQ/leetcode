class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        result = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j == i:
                        dp[i][j] = 1
                    elif j == i + 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    if j == i + 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                result = max(result, dp[i][j])
        return result

# Comment:
# This is a dynamic programming solution.
# We use a 2D array dp to store the length of the longest palindromic subsequence.
# dp[i][j] represents the length of the longest palindromic subsequence of the substring s[i:j+1].

# In initialization, we set dp[i][i] = 1 for all i, because a single character is a palindromic subsequence.
# Then we iterate the string s from the end to the start, because we need to use the values of dp[i+1][j-1] and dp[i][j-1] to calculate dp[i][j].
# If s[i] == s[j], we divide the problem into three cases:
# 1. If i == j, the length of the palindromic subsequence is 1.
# 2. If j == i + 1, the length of the palindromic subsequence is 2.
# 3. Otherwise, the length of the palindromic subsequence is dp[i+1][j-1] + 2.

# If s[i] != s[j], we divide the problem into two cases:
# 1. If j == i + 1, the length of the palindromic subsequence is 1.
# 2. Otherwise, the length of the palindromic subsequence is max(dp[i][j-1], dp[i+1][j]).

# Finally, we return the maximum value in the dp array as the result.

# Time complexity: O(n^2), where n is the length of the input string s.
# Space complexity: O(n^2), where n is the length of the input string s.

# We can start j from i + 1 to avoid if j == i condition, and make this solution more concise.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        result = 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                result = max(result, dp[i][j])
        return result

# Note we have dp[i][j] == 0 in the lower triangle of the dp array, so when j-1 > i+1, we have dp[i+1][j-1] == 0, and we can simplify the code.
# This solution is more concise and easier to understand.
    
