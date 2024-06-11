class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))

# Comment:
# 使用set寻找交集
# 时间复杂度：O(m + n)
# 空间复杂度: O(n)

# 注：需要查证，set()操作的时间/空间复杂度