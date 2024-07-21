from typing import List

class Solution:
    def backtracking(self, nums, path, result):
        if len(nums) == len(path):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.backtracking(nums, path, result)
                path.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [], result)
        return result


# Test cases
nums = [1,2,3]
solution = Solution()
print(solution.permute(nums)) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# Comment:
# This problem is similar to 90-subsets-ii, but with a different condition to generate the subsets.
# We may have a better pruning strategy for this problem.
# For instance, we can store all the used indexes in a set, and in the condition of the loop, we can exlude the indexes that have been used.
