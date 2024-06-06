class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        while(i < l):
            if nums[i] == val:
                for j in range(i, l-1):
                    nums[j] = nums[j+1]
                i -= 1
                l -= 1
            i += 1
        return l

# Comment: 暴力算法，外层循环为从头遍历数组，遍历长度为目前没有删去的元素的个数，随着逐渐删除而减少。
# 内层循环为找到一个目标值后，将后面的元素依次向前移动一位。
# 完成后, i减一，因为当前位置的元素已经被替换，下次循环时需要重新检查，需要和例行+1抵消。
# l减一，因为有一个元素被删除了。