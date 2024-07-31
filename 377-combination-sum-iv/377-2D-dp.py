class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums)+ 1):
            dp[i][0] = 1

        for j in range(1, target + 1):
            for i, num in enumerate(nums, 1):
                dp[i][j] = dp[i-1][j]
                if j >= num:
                    dp[i][j] += dp[-1][j-num]
        return dp[len(nums)][target]

# Comment:
# This problem is permutation.
# So we need to consider the order of the elements in the combination.

# The order of the iteration is important.
# And it should be first knapsack capacity, then items.


