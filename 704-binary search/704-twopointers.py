# 方法1：左闭右开区间
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while(left < right):
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1
    
# Comment:  左闭右开区间， 想能否取等时，想[n,n)能否取到值，答案是不能，所以不取等
# 时间复杂度：O(logn)
# 空间复杂度：O(1)


# 方法2：左闭右闭区间
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while(left<=right):
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1
    
# Comment:  左闭右闭区间， 想能否取等时，想[n,n]能否取到值，答案是可以，所以取等
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
