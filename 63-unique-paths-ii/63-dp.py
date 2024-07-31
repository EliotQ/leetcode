class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][n-1] == 1:
                for k in range(i, -1, -1):
                    dp[k][n-1] = 0
                break
        for j in range(n-1, -1, -1):
            if obstacleGrid[m-1][j] == 1:
                for k in range(j, -1, -1):
                    dp[m-1][k] = 0
                break

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                else:
                    dp[i][j] = 0
        return dp[0][0]

# We use the same idea as 62-unique-paths/62-dp.py, but we need to consider the obstacleGrid.
# We first initialize the dp array with 1s, because for the last row and the last column, there is only one way to reach the end.
# Considering the obstacle, if the last row has an obstacle, we need to set all the cells in that cell and the cells left to it in the last row to 0.
# If the last column has an obstacle, we need to set all the cells in that cell and the cells above it in the last column to 0.

# Time complexity: O(m*n)
# Space complexity: O(m*n)