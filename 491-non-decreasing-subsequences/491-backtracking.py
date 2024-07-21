from typing import List
class Solution:
    def backtracking(self, nums, path, start_index, result):
        if len(path) >= 2:
            result.append(path[:])
        used_set = set()
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] in used_set:
                continue
            if len(path) >= 1 and nums[i] < path[-1]:
                continue
            used_set.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, path, i + 1, result)
            path.pop()
            
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [], 0, result)
        return result

        
# Test cases
nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
solution = Solution()
print(solution.findSubsequences(nums)) #

# Comment:
# This problem is similar to 90-subsets-ii, but with a different condition to generate the subsets.
# In order to skip the same value in the same level, we need to use a set to store the used values.
# which is relatively new because what we use to avoid same-level duplicates in 90-subsets-ii is to compare the current value with the previous value.
# i.e. nums[i] == nums[i-1]
# But this time, we need to compare the current value with all the values in the current level,
# because we should not sort the input array.