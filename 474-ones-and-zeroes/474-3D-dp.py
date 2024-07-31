class Solution:    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        
        for i in range(1, len(strs)+1):
            num_0 = strs[i-1].count('0')
            num_1 = strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= num_0 and k >= num_1:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-num_0][k-num_1] + 1)
        return dp[len(strs)][m][n]

# Comment:
# Using dynamic programming to solve this problem.
# Time complexity: O(l*m*n), where l is the length of the array, m is the maximum number of 0s, and n is the maximum number of 1s.
# Space complexity: O(l*m*n), where l is the length of the array, m is the maximum number of 0s, and n is the maximum number of 1s.

# We can see that i only depends on i-1, so we can reduce the space complexity to O(m*n).
# See 474-2D-dp.py for the solution.