class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < abs(target):
            return 0
        if (sum(nums) + target) % 2 != 0:
            return 0
        target_sum = (sum(nums) + target) // 2
        dp = [[0]*(target_sum + 1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(target_sum + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[len(nums)][target_sum]

# Comment:
# Using dynamic programming to solve this problem.
# We notice, if we divide the array into two subsets, "+ left" and "- right", we have:
# sum(left) - sum(right) = target
# sum(left) + sum(right) = sum(nums)
# So we have:
# sum(left) = (sum(nums) + target) // 2
# This is a 0/1 knapsack problem.
# We set the maximum capacity of the knapsack to be (sum(nums) + target) // 2.
# And we regard each number in the array as an item with a weight equal to its value.
# And this becomes similar to 416-partition-equal-subset-sum/416-dp.py.

# Can do this with a 1D dp array. 
# Leave for later.

# Time complexity: O(n*target_sum), where n is the length of the array.
# Space complexity: O(n*target_sum), where n is the length of the array.