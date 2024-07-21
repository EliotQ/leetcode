class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        count = 1
        cur_diff = 0
        pre_diff = 0

        for i in range(len(nums) - 1):
            cur_diff =  nums[i + 1] - nums[i]
            if (cur_diff < 0 and pre_diff >= 0) or (cur_diff > 0 and pre_diff <= 0):
                count += 1
                pre_diff = cur_diff
        return count

# Complexity Analysis
# Time complexity: O(n), where n is the length of nums.
# Space complexity: O(1).

# Here we are using a greedy approach to solve the problem. We keep a count of the number of elements in the wiggle subsequence. We also keep track of the difference between the current element and the previous element. If the difference changes sign, we increment the count. We return the count as the answer.