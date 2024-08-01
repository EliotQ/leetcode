class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        result = 1
        left = 0
        right = 1

        while(right <= len(nums) - 1):
            if nums[right] > nums[right-1]:
                result = max(right - left + 1, result)
                right += 1
            else:
                left = right 
                right = left + 1
        return result

# Comment:
# Using two pointers to solve this problem.

# Time complexity: O(n)
# Space complexity: O(1)