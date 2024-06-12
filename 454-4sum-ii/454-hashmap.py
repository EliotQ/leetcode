class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import defaultdict
        sum_dict = defaultdict(int)
        ans = 0

        n = len(nums1)
        for i in range(n):
            for j in range(n):
                sum_dict[nums1[i] + nums2[j]] += 1
        
        for i in range(n):
            for j in range(n):
                targert = - (nums3[i] + nums4[j])
                ans += sum_dict[targert]
        return ans

# Comment:
# 分组+哈希表
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)