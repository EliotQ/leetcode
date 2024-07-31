class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums += nums
        result = [-1] * len(nums)
        stack = [0]

        for i in range(len(nums)):
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while(len(stack) > 0 and nums[i] > nums[stack[-1]]):
                    result[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        return result[:length]

# Comment:
# Use a monotonic stack to find the next greater element for each element in the circular array.
# The array is extended by concatenating it with itself to handle the circular property.
# The stack maintains the indices of elements that are yet to find the next greater element.
# If an element is lower than or equal to the element at the top of the stack, it is added to the stack.
# If an element is higher than the element at the top of the stack, it means the next greater element has been found.
# In this case, the function pops elements from the stack and calculates the next greater element for each popped element.
# The result is stored in a list with the corresponding index in the original array.
# Finally, the function returns the result for the original array.

# Time complexity: O(n), where n is the length of the input array nums
# Space complexity: O(n), where n is the length of the input array nums