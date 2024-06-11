class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = [0] * 1001
        counter2 = [0] * 1001
        res = []

        for i in nums1:
            counter1[i] += 1
        for i in nums2:
            counter2[i] += 1
        
        for i in range(1001):
            if counter1[i] * counter2[i] > 0:
                res.append(i)
        return res

# Comment:
# 题目条件：
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 可以把数组当做hashmap使用
# 时间复杂度：O(m + n)
# 空间复杂度: O(n)