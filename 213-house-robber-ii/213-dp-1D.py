class Solution:
    def rob_range(self, nums, start, end):
        nums = nums[start:end]
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[len(nums)-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        result_no_first = self.rob_range(nums, 1, len(nums))
        result_no_last = self.rob_range(nums, 0, len(nums) - 1)
        
        return max(result_no_first, result_no_last)

# Comment:
# We can't rob the first and last houses at the same time, so we have two choices:
# 1. Rob the first house, then we can't rob the last house, so the money we get is self.rob_range(nums, 0, len(nums) - 1)
# 2. Don't rob the first house, then the money we get is self.rob_range(nums, 1, len(nums))

# Time complexity: O(n)
# Space complexity: O(n)