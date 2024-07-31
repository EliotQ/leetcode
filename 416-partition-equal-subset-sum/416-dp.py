class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        n = sum(nums) // 2
        dp = [[0] * (n+1) for _ in range(len(nums))]

        for j in range(n+1):
            if j > nums[0]:
                dp[0][j] = nums[0]
        
        for i in range(1, len(nums)):
            for j in range(1, n+1):
                if j >= nums[i]:
                    dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-1][j - nums[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums) - 1][n] == n

# Comment:
# Dynamic programming (based on 0/1 knapsack problem)
# We set the maximum capacity of the knapsack to be sum(nums) // 2. 
# And we regard each number in the array as an item with a weight equal to its value.
# If the maximum value of the knapsack is equal to sum(nums) // 2, we can partition the array into two subsets with the same sum.
# Time complexity: O(n * len(nums))
# Space complexity: O(n * len(nums))
