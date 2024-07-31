class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = [0]
        
        for i in range(1, len(nums) * 2):
            if nums[i%len(nums)] <= nums[stack[-1]]:
                stack.append(i%len(nums))
            else:
                while(len(stack) > 0 and nums[i%len(nums)] > nums[stack[-1]]):
                    result[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
                stack.append(i%len(nums))
        return result

# Comment:
# Use a monotonic stack to find the next greater element for each element in the circular array.
# Compared with 503-monotonic-stack.py, the array is not extended by concatenating it with itself to handle the circular property.
# Instead, the index is calculated as i%len(nums) to simulate the circular property.

# Time complexity: O(n), where n is the length of the input array nums
# Space complexity: O(n), where n is the length of the input array nums
# Another implementation:

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = [0]
        
        for i in range(1, len(nums) * 2):
            i = i % len(nums)
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while(len(stack) > 0 and nums[i] > nums[stack[-1]]):
                    result[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        return result
    
# Another implementation:
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = [0]
        
        for i in range(1, len(nums) * 2):
            i = i % len(nums)
            while(len(stack) > 0 and nums[i] > nums[stack[-1]]):
                result[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return result

# Remove the redundant if statement in the while loop.