class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[-1]

# Comment:
# Dynamic Programming
# Time complexity: O(n)
# Space complexity: O(n)

# Here we can omit the dp array and only keep the last two numbers, because we only need the last two numbers to calculate the next number.