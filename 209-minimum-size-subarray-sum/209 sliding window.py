class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        cur_min_len = len(nums) + 1
        cur_sum = 0

        while(right < len(nums)):
            cur_sum += nums[right]
            while(cur_sum >= target):
                cur_min_len = min(cur_min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        if cur_min_len == len(nums) + 1:
            return 0
        return cur_min_len

# Comment:使用滑动窗口，当窗口内的和大于等于target时，缩小窗口，直到窗口内的和小于target，
# 然后扩大窗口，直到窗口内的和大于等于target，如此循环，直到right到达数组末尾。

# 需要用cur_sum记录窗口内的和，否则每次都要重新计算窗口内的和，会超时。
#（时间复杂度增加了，考虑最坏情况，左指针一直不动，右指针一直移动，每次都要重新计算窗口内的和，时间复杂度为O(n^2)）

# 时间复杂度为O(n)。
# 空间复杂度为O(1)。