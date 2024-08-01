class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[len(word1)][len(word2)]

# Comment:
# In this solution, we find the minimum number of operations to make word1 and word2 the same.
# dp[i][j] represents the minimum number of operations to make the first i characters of word1 and the first j characters of word2 the same.
# In initialization, we consider how many operations to make the first i characters of word1 and the first 0 characters of word2 the same.
# We need to delete i characters from word1 to make the first i characters of word1 and the first 0 characters of word2 the same.

# Transition function:
# dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1], because we don't need to do any operation if word1[i-1] == word2[j-1]
# dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1) if word1[i-1] != word2[j-1], because we need to delete word1[i-1] or word2[j-1] to make them the same.

# Time complexity: O(m*n)
# Space complexity: O(m*n)
