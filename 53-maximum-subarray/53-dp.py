class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result

# Comment:
# using dynamic programming to solve this problem
# transition function: dp[i] = max(dp[i-1] + nums[i], nums[i])

# Time complexity: O(n)
# Space complexity: O(n)