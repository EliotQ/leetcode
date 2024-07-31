class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = sum(stones) // 2
        dp = [[0]*(n+1) for _ in range(len(stones))]
        for j in range(n+1):
            if j >= stones[0]:
                dp[0][j] = stones[0]

        for i in range(1, len(stones)):
            for j in range(1, n+1):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i-1][j], stones[i] + dp[i-1][j-stones[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return sum(stones) - 2 * dp[-1][-1]

# Comment:
# Dynamic programming (based on 0/1 knapsack problem)
# similar to 416-partition-equal-subset-sum/416-dp.py
# Time complexity: O(n * len(stones))
# Space complexity: O(n * len(stones)

# We use the same idea as 416-partition-equal-subset-sum/416-dp.py to solve this problem.
# We set the maximum capacity of the knapsack to be sum(stones) // 2.
# And we regard each number in the array as an item with a weight equal to its value.
# The maximum value of the knapsack is the optimal segmentation of the stones into two groups.
# The difference between the two groups is the answer to this problem.