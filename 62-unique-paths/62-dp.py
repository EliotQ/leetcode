class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

# Comment:
# Here we use dynamic programming to solve this problem.

# Time complexity: O(m*n)
# Space complexity: O(m*n)

# First, we determine the length of the dp array, which is m*n. 
# Then we initialize the dp array with 1s. 
# We iterate through the dp array from the next-to-last row to the first row and from the next-to-last column to the first column. That said, the range of i is from m-2 to 0, and the range of j is from n-2 to 0.
# For each cell, we calculate the number of unique paths to reach the bottom right corner from that cell. The number of unique paths to reach the bottom right corner from a cell is the sum of the number of unique paths to reach the cell below it and the number of unique paths to reach the cell to the right of it. Finally, we return the number of unique paths to reach the bottom right corner from the top left corner.