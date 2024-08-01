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
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[len(word1)][len(word2)]

# Comment:
# In this solution, we find the minimum number of operations to make word1 and word2 the same.
# dp[i][j] represents the minimum number of operations to make the first i characters of word1 and the first j characters of word2 the same.

# In initialization, we consider how many operations to make the first i characters of word1 and the first 0 characters of word2 the same.
# We need to delete i characters from word1 to make the first i characters of word1 and the first 0 characters of word2 the same.
# And we need to insert i characters to make the first 0 characters of word1 and the first i characters of word2 the same.
# So dp[i][0] = i and dp[0][j] = j for all i and j.

# Transition function:
# dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1], because we don't need to do any operation if word1[i-1] == word2[j-1]
# In case word1[i-1] != word2[j-1], 

# if we want to modify word1, we have three options:
# 1. Delete word1[i-1]: dp[i][j] = dp[i-1][j] + 1
# 2. Insert word2[j-1] to word1: dp[i][j] = dp[i][j-1] + 1
# 3. Replace word1[i-1] with word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1

# if we want to modify word2, we have three options:
# 1. Delete word2[j-1]: dp[i][j] = dp[i][j-1] + 1
# 2. Insert word1[i-1] to word2: dp[i][j] = dp[i-1][j] + 1
# 3. Replace word2[j-1] with word1[i-1]: dp[i][j] = dp[i-1][j-1] + 1

# We can see that the three options to modify word1 and the three options to modify word2 are symmetric.
# i.e delete word1[i-1] is the same as insert word1[i-1] to word2, and 
#     delete word2[j-1] is the same as insert word2[j-1] to word1, and
#     replace word1[i-1] with word2[j-1] is the same as replace word2[j-1] with word1[i-1].
# So we can simplify the transition function to:
# dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1) if word1[i-1] != word2[j-1]
# quick hint: three option: delete 1, delete 2, replace.

# Time complexity: O(m*n)
# Space complexity: O(m*n)