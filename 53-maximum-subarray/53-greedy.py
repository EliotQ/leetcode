class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')

        for i in nums:
            cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
            
# Complexity Analysis
# Time complexity: O(n), where n is the length of nums.
# Space complexity: O(1).