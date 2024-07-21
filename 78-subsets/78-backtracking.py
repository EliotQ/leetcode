import sys
from typing import List

class Solution:
    def backtracking(self, nums, cur_set, start_index,  result):
        result.append(cur_set[:])
        for i in range(start_index, len(nums)):
            start_index = i + 1
            cur_set.append(nums[i])
            self.backtracking(nums, cur_set, start_index, result) 
            cur_set.pop()

            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [], 0, result)
        return result
    
# Test case:
nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))

# When "cutting" the input, we use the start_index, instead of slicing the input array.
# This is to avoid duplicate or missing subsets, because when using slicing, the input array is changed.

# This wrong answer can be further investigated if have more time:

# class Solution:
#     def backtracking(self, nums, cur_set, result):
#         if len(nums) == 0:
#             result.append(cur_set[:])
#             return
# 
#         for i in range(len(nums) - 1):
#             self.backtracking(nums[i+1:], cur_set, result)
# 
#             cur_set.append(nums[i])
#             self.backtracking(nums[i+1:], cur_set, result) 
#             cur_set.pop()
# 
#              
#             
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         self.backtracking(nums, [], result)
#         return result
