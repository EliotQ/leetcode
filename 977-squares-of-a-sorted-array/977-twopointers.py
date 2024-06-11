# leetcode 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = []

        while(left <= right):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square >= right_square:
                ans.append(left_square)
                left += 1
            else:
                ans.append(right_square)
                right -= 1
            
        return ans[::-1]
# Comment: 本题是一个简单的双指针问题，由于数组是有序的，所以最大的平方值一定在数组的两端。
# 依次比较两端的平方值，将较大的值添加到结果数组的末尾，然后移动指针。
# 结束条件为左闭右闭区间，如果左指针等于右指针，依然有意义，所以需要取等。
# 时间复杂度：O(n)
# 空间复杂度：存疑，不确定切片是否需要额外空间，如果需要，空间复杂度为O(n)。待验证。