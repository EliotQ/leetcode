from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        result = 0

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
                result = max(result, dp[i][j])
        print(dp)
        return result

s = Solution()
text1 = "abcde"
text2 = "ace"

print(s.longestCommonSubsequence(text1, text2)) # 3

# Comment:
# Using dynamic programming
# dp[i][j] represents the length of longest common subsequence that considered the first i-th digit of text1 and the first j-th digit of text2
# The transition function is:
# if text1[i-1] == text2[j-1], then the common subsequence can be prolonged with the current i-th digit and j-th digit, and leads to
#   dp[i][j] = dp[i-1][j-1] + 1
# else text1[i-1] != text2[j-1], then the common subsequence can not be prolonged with the current i-th digit and j-th digit, and leads to
#   dp[i][j] = max(dp[i][j-1],dp[i-1][j])
# here we use max(dp[i][j-1],dp[i-1][j]) because we need to consider the situation that the length of common subsequence is different when we consider the 
#   1) first i-th digit of text1 and the (j-1)-th digit of text2
#   2) first (i-1)-th digit of text1 and the j-th digit of text2

# example:
# text1 = "ebcde"
# text2 = "bcf"
# we have dp[2][2] = 1, dp[2][3] = 1, dp[3][2] = 2
# and we want to calculate dp[3][3]
# text1[3] != text2[3], and here dp[3][3] = max(dp[3][2],dp[2][3]) = 2
# this justifies the reason why we use max(dp[i][j-1],dp[i-1][j]) in the transition function


# Time complexity: O(m*n)
# Space complexity: O(m*n)


