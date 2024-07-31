class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(len(strs)):
            zero_count = strs[i].count('0')
            one_count = strs[i].count('1')
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= zero_count and k >= one_count:
                        dp[j][k] = max(dp[j][k], dp[j-zero_count][k-one_count]+1)
        
        return dp[m][n]

# Comment:
# Using dynamic programming to solve this problem.
# Time complexity: O(l*m*n), where l is the length of the array, m is the maximum number of 0s, and n is the maximum number of 1s.
# Space complexity: O(m*n), where m is the maximum number of 0s, and n is the maximum number of 1s.

# We should note that, when we overwrite the dp array, we should iterate from the end to the beginning.
# This is because we are using the previous values to update the current value.
# If we iterate from the beginning to the end, we may use the updated values to update the current value.
# This will cause 'repeated use' of the same value, which is not correct.