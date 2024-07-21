class Solution:
    def backtracking(self, nums, path, used,  result):
        if len(nums) == len(path):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if (i > 0 and nums[i-1] == nums[i] and not used[i-1]):
                continue 

            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used,  result)
            path.pop()
            used[i] = False
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backtracking(nums, [], [False] * len(nums), result)
        return result

# Comment:
# Compared to 46-permutations/46-backtracking.py, we need to sort the input array first.
# We also need to add a condition to skip the duplicate numbers.
# The condition is: if the current number is the same as the previous number, and the previous number is not used, then skip the current number.
# This is pruning at the same level of the tree.

# instead, we can prune at different levels of the tree, by using

# if (i > 0 and nums[i-1] == nums[i] and used[i-1]):
#                 continue 

# By using this condition, we allow this tree to grow one more level compared to the previous condition.