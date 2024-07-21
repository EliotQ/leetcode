class Solution:
    def backtracking(self, nums, cur_subset, start_index, result):
        result.append(cur_subset[:])

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i-1]:
                continue
            cur_subset.append(nums[i])
            self.backtracking(nums, cur_subset, i + 1, result)
            cur_subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backtracking(nums, [], 0, result)
        return result

# Comment:
# This problem is similar to 78-subsets, but with duplicates in the input array.
# To avoid duplicates in the result, we need to sort the input array first. (just like in 40-combination-sum-ii)
# Then, we need to skip the duplicates in the input array when generating the subsets.

# Time complexity: O(2^n)
# Space complexity: O(n) for the recursion stack
        
