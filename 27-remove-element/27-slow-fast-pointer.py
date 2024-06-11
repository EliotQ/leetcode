# 算法1， 只检查快指针，如果快指针指向的元素不等于目标值，就将快指针指向的元素赋值给慢指针，然后慢指针+1，快指针+1。
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0

        while(fast < len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# Comment: 这种方法比较简洁，只需要检查一个指针，前提是快慢指针的起点相同。
# 时间复杂度：O(n)
# 空间复杂度：O(1)


# 算法2，检查慢指针，如果慢指针指向的元素等于目标值，就将快指针移到不为目标值的元素位置，然后将快指针指向的元素赋值给慢指针，然后慢指针+1，快指针+1。
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while(fast < len(nums)):
            if nums[slow] == val:
                if nums[fast] == val:
                    fast += 1
                    continue
                else:
                    nums[slow] = nums[fast]
                    nums[fast] = val
            slow += 1
            fast += 1
        return slow

# Comment: 这种方法比较符合直觉，但是比较繁琐，需要检查两个指针。
# 时间复杂度：O(n)
# 空间复杂度：O(1)