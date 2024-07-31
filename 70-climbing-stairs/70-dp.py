class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Comment:
# Dynamic Programming
# Time complexity: O(n)
# Space complexity: O(n)

# Here we can omit the dp array and only keep the last two numbers, because we only need the last two numbers to calculate the next number.