class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        result = max(dp)
        return result

# Comment:
# Using dynamic programming to solve this problem
# dp[i] represents the length of longest continuous increseaing subsequence ends with the i-th digit
# THe transition function is:
# if nums[i-1] < nums[i]: then this subsequence can be prolonged with current i-th digit, and dp[i] = dp[i-1] + 1
# else nums[i-1] >= nums[i]: this subsequence should start again with i-th digit, and dp[i] = 1