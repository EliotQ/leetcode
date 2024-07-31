class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[len(nums) - 1]

# Comment:
# The transition function is dp[i] = max(dp[i-1], dp[i-2] + nums[i])
# Because we can't rob two adjacent houses, we have two choices:
# 1. Rob the current house, then we can't rob the previous house, so the money we get is dp[i-2] + nums[i]
# 2. Don't rob the current house, then the money we get is dp[i-1]. Note here it doesn't mean we have to rob the previous house, it just means we have the choice to rob it or not.

# Time complexity: O(n)
# Space complexity: O(n)