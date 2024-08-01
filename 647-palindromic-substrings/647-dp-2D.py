class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        result = 0
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if i == j:
                        dp[i][j] = 1
                        result += 1
                    elif i + 1 == j:
                        dp[i][j] = 1
                        result += 1
                    else:
                        if dp[i+1][j-1] == 1:
                            dp[i][j] = 1
                            result += 1
                        else:
                            dp[i][j] = 0
                else:
                    dp[i][j] = 0
        
        return result

# Comment:
# This is a dynamic programming solution.
# we use a 2D array dp to store whether the substring s[i:j+1] is palindromic.
# In initialization, we set dp[i][i] = 1 for all i, because a single character is palindromic.
# Then we iterate the string s from the end to the start.
# For each pair of indices i and j, we check whether s[i] == s[j].
# If they are equal, we divide the problem into three cases:
# 1. i == j, which means the substring is a single character, so it is palindromic.
# 2. i + 1 == j, which means the substring has two characters, so it is palindromic.
# 3. Otherwise, we check whether the substring s[i+1:j] is palindromic.
#   If it is, then the substring s[i:j+1] is palindromic.
#   Otherwise, it is not palindromic.
# If they are not equal, the substring is not palindromic.

# Time complexity: O(n^2)
# Space complexity: O(n^2)