class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        result = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

# Comment:
# Using dynamic programming
# Time complexity: O(n^2)
# Space complexity: O(n)

# Attention: do not omit the condition that if nums[i] > nums[j] in the inner loop