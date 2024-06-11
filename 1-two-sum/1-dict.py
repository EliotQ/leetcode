class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = dict()
        for idx, val in enumerate(nums):
            if target - val in idx_dict:
                return [idx, idx_dict[target - val]]
            idx_dict[val] = idx
        return []

# Comment:
# 使用dict存储，key: 数字，value: index