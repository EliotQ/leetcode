class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        left = 0
        while(left < len(nums) - 2):
            if left >= 1 and nums[left-1] == nums[left]:
                left += 1
                continue
            
            mid = left + 1
            right = len(nums) - 1
            while(mid < right):
                res = nums[left] + nums[mid] + nums[right]
                if res > 0:
                    right -= 1
                    while(right > mid + 1 and nums[right] == nums[right + 1]):
                        right -= 1
                elif res < 0:
                    mid += 1
                    while(right > mid + 1 and nums[mid] == nums[mid - 1]):
                        mid += 1
                else:
                    ans.append([nums[left], nums[mid], nums[right]])
                    right -= 1
                    while(right > mid + 1 and nums[right] == nums[right + 1]):
                        right -= 1
                    mid += 1
                    while(right > mid + 1 and nums[mid] == nums[mid - 1]):
                        mid += 1
            left += 1
        return ans

# Comment:
# 三指针
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)，排序的空间复杂度 （不考虑返回值的空间复杂度，返回值的空间复杂度为O(n^3)，最坏情况下为C(n,3)，即O(n^3)）