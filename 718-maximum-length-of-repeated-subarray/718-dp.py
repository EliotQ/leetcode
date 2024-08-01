class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        result = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(result, dp[i][j])
        return result

# Comment:
# Here we are trying to find the longest "continuous" subarray in two arrays, which is not clear in the problem description.
# The result of [1,2,1,2,1] and [1,3,1,3,1] is 1.(by adding this as a test case on leetcode.)

# Compare this with 1143-longest-common-subsequence, where the subarray does not need to be continuous.

# Using dynamic programming
# dp[i][j] represents the length of longest common subarray that ends with the i-th digit of nums1 and the j-th digit of nums2
# The transition function is:
# if nums1[i-1] == nums2[j-1], then the common subarray can be prolonged with the current i-th digit and j-th digit, and leads to
#   dp[i][j] = dp[i-1][j-1] + 1

# Time complexity: O(m*n)
# Space complexity: O(m*n)